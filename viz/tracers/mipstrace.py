"""code-viz MIPS tracer (mipstrace.py): assemble a MIPS32 program and run it instruction by instruction,
recording the registers and every memory write, for the viewer's register-and-memory view.

Full manual: the header of code-viz (`code-viz readme`, or README.md), sections 7 Kinds of
visualization (mips) and 14 Trace format.

WHERE IT RUNS
  In the mips runner container (driver.py, viz=mips), where SPIM also runs the same program as the
  reference: when SPIM's output differs from this simulator's, the trace is marked approximate and
  shows SPIM's output (as the Scheme tracer does with Guile). It is pure Python (standard library
  only), so the viewer also loads it into Pyodide for student mode's Edit and run.

WHAT IT SUPPORTS (the subset CS274 teaches, which is what SPIM and MARS run)
  Directives: .data .text .globl .word .half .byte .ascii .asciiz .space .align, labels, comments (#).
  Instructions: add addu sub subu and or xor nor slt sltu sll srl sra sllv srlv srav, addi addiu andi
  ori xori slti sltiu lui, lw sw lh lhu sh lb lbu sb, beq bne blez bgtz bltz bgez, j jal jr jalr,
  mult multu div divu mfhi mflo mthi mtlo, syscall, nop; pseudo-instructions li la move b beqz bnez
  blt bgt ble bge bltu bgtu bleu bgeu mul div rem (three operands) neg negu not abs seq sne sgt sge sle.
  Syscalls: 1 print int, 4 print string, 5 read int, 8 read string, 9 sbrk, 10 exit, 11 print char,
  12 read char, 17 exit with code, 34 print hex, 35 print binary, 36 print unsigned. Input for 5, 8
  and 12 comes from the label's input="..." (one line per read).
  Memory layout as in MARS: text at 0x00400000 (main is the first instruction; SPIM runs a few start-up
  instructions first and puts main at 0x00400024, so text addresses differ from SPIM's by that much),
  static data at 0x10010000, heap after it (sbrk), $gp 0x10008000, $sp 0x7fffeffc.
  Arithmetic overflow traps (add, addi, sub) are not raised; results wrap, as with addu.

TRACE (kind "mips")
  {"version": 1, "kind": "mips", "language": "mips", "source": program text,
   "labels": {name: address}, "data": {"base": 0x10010000, "hex": initial data bytes},
   "regs0": [34 initial values: $0..$31, hi, lo],
   "steps": [{"line": source line, "pc": address, "ins": instruction text, "regs": {index: new value} (changed only),
              "mem": [[address, size, value], ...] (writes), "out": length of stdout so far}],
   "stdout": ..., "error": message or null, "truncated": bool}

USAGE
  python3 mipstrace.py prog.s [--max-steps 800] [--input "lines"]    # prints the trace as JSON
  trace_source(src, inp="", max_steps=800)                            # the same, from Python (Pyodide)
"""
import argparse
import json
import re
import sys

REGS = ["zero", "at", "v0", "v1", "a0", "a1", "a2", "a3", "t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7",
        "s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "t8", "t9", "k0", "k1", "gp", "sp", "fp", "ra"]
RNUM = {n: i for i, n in enumerate(REGS)}
RNUM["s8"] = 30
TEXT, DATA, GP, SP = 0x00400000, 0x10010000, 0x10008000, 0x7FFFEFFC
M32 = 0xFFFFFFFF
IMM_OF = {"add": "addi", "addu": "addiu", "sub": "addi", "subu": "addiu", "and": "andi", "or": "ori", "xor": "xori",
          "slt": "slti", "sltu": "sltiu"}


class AsmError(Exception):
    pass


def s32(x):
    x &= M32
    return x - (1 << 32) if x & 0x80000000 else x


def reg(tok, line):
    t = tok.strip().lstrip("$")
    if t.isdigit() and int(t) < 32:
        return int(t)
    if t in RNUM:
        return RNUM[t]
    raise AsmError(f"line {line}: not a register: {tok}")


def unescape(s):
    return bytes(s, "utf-8").decode("unicode_escape").encode("latin-1")


def split_ops(rest):
    out, cur, q = [], "", False
    for ch in rest:
        if ch == '"':
            q = not q
        if ch == "," and not q:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def strip_comment(line):
    out, q = "", False
    for ch in line:
        if ch == '"':
            q = not q
        if ch == "#" and not q:
            break
        out += ch
    return out


class Program:
    def __init__(self, src):
        self.src = src
        self.labels = {}
        self.text = []          # [(line, mnemonic, ops)] one entry per machine word (pseudo-ops expanded later)
        self.data = bytearray()
        self.parse()

    def parse(self):
        seg = "text"
        items = []              # (seg, line, kind, value)
        for n, raw in enumerate(self.src.split("\n"), 1):
            line = strip_comment(raw).strip()
            while True:
                m = re.match(r"^([A-Za-z_.$][\w.$]*)\s*:\s*(.*)$", line)
                if not m:
                    break
                items.append((seg, n, "label", m.group(1)))
                line = m.group(2).strip()
            if not line:
                continue
            if line.startswith("."):
                d, _, rest = line.partition(" ")
                d = d.lower()
                rest = rest.strip()
                if d in (".text", ".ktext"):
                    seg = "text"
                elif d in (".data", ".kdata", ".rdata", ".sdata"):
                    seg = "data"
                elif d in (".globl", ".global", ".extern", ".set", ".ent", ".end", ".type", ".size", ".file"):
                    pass
                else:
                    items.append(("data", n, d, rest))
                continue
            mn, _, rest = line.partition(" ")
            items.append((seg, n, "ins", (mn.lower(), split_ops(rest.strip()))))
        # pass 1: addresses
        pc, dp = TEXT, DATA
        layout = []
        pending = []            # data labels not yet followed by data: they move with alignment padding
        for seg, n, kind, val in items:
            if kind == "label":
                self.labels[val] = pc if seg == "text" else dp
                if seg == "data":
                    pending.append(val)
                continue
            if kind == "ins":
                size = 4 * self.words(val[0], val[1], n)
                layout.append((pc, n, val))
                pc += size
                continue
            # data directives
            d, rest = kind, val
            if d == ".align":
                a = 1 << int(rest or "2", 0)
                pad = (-dp) % a
                self.data += bytes(pad)
                dp += pad
                for lab in pending:          # labels above an .align point at the aligned address
                    self.labels[lab] = dp
                continue
            if d in (".word", ".half", ".byte"):
                size = {".word": 4, ".half": 2, ".byte": 1}[d]
                pad = (-dp) % size
                self.data += bytes(pad)
                dp += pad
                for lab in pending:
                    self.labels[lab] = dp
                pending = []
                for tok in split_ops(rest):
                    if ":" in tok:
                        v, cnt = tok.split(":")
                        vals = [v.strip()] * int(cnt, 0)
                    else:
                        vals = [tok]
                    for v in vals:
                        self.data += b"\0" * size  # filled in pass 2 (labels may come later)
                        layout.append(("data", dp, size, v, n))
                        dp += size
                continue
            pending = []
            if d in (".ascii", ".asciiz"):
                m = re.match(r'^"(.*)"$', rest)
                if not m:
                    raise AsmError(f"line {n}: {d} needs a quoted string")
                b = unescape(m.group(1)) + (b"\0" if d == ".asciiz" else b"")
                self.data += b
                dp += len(b)
                continue
            if d == ".space":
                k = int(rest, 0)
                self.data += bytes(k)
                dp += k
                continue
            raise AsmError(f"line {n}: unsupported directive {d}")
        # labels declared on the line before a .word that had padding point at the padded word: SPIM does the same
        self.code = []
        for e in layout:
            if e[0] == "data":
                _, addr, size, v, n = e
                val = self.value(v, n)
                self.data[addr - DATA:addr - DATA + size] = (val & ((1 << (8 * size)) - 1)).to_bytes(size, "little")
            else:
                addr, n, (mn, ops) = e
                self.code.append((addr, n, self.expand(mn, ops, n, addr), 4 * self.words(mn, ops, n)))
        self.at = {a: (n, w, size) for a, n, w, size in self.code}
        self.end = pc

    def value(self, tok, n):
        tok = tok.strip()
        m = re.match(r"^([A-Za-z_.$][\w.$]*)\s*([+-]\s*\d+)?$", tok)
        if m and not re.match(r"^-?(0x[0-9a-f]+|\d+)$", tok, re.I):
            if m.group(1) not in self.labels:
                raise AsmError(f"line {n}: unknown label {m.group(1)}")
            return self.labels[m.group(1)] + int((m.group(2) or "0").replace(" ", ""))
        if re.match(r"^'.'$", tok):
            return ord(tok[1])
        try:
            return int(tok, 0)
        except ValueError:
            raise AsmError(f"line {n}: not a number or label: {tok}")

    def words(self, mn, ops, n):
        if mn in ("li",):
            try:
                v = int(ops[1], 0)
            except (ValueError, IndexError):
                return 2
            return 1 if -32768 <= v <= 65535 else 2
        if mn == "la":
            return 2
        if mn in ("blt", "bgt", "ble", "bge", "bltu", "bgtu", "bleu", "bgeu", "seq", "sne", "sge", "sle", "abs"):
            return 2
        if mn in ("mul", "div", "divu", "rem", "remu") and len(ops) == 3:
            return 2
        if mn in ("lw", "sw", "lb", "lbu", "sb", "lh", "lhu", "sh") and len(ops) == 2 and not re.search(r"\(", ops[1]):
            return 2
        return 1

    def expand(self, mn, ops, n, addr):
        """The operation (a tuple) for a source instruction; pseudo-instructions are one operation."""
        return self._expand(mn, ops, n, addr)[0]

    def _expand(self, mn, ops, n, addr):
        r = lambda i: reg(ops[i], n)  # noqa: E731
        v = lambda i: self.value(ops[i], n)  # noqa: E731
        def fill(ws):
            return ws
        try:
            if mn == "nop":
                return [("nop",)]
            if mn == "syscall":
                return [("syscall",)]
            if mn in ("add", "addu", "sub", "subu", "and", "or", "xor", "nor", "slt", "sltu", "sllv", "srlv", "srav"):
                if mn in IMM_OF and not ops[2].startswith("$"):
                    return fill([(IMM_OF[mn], r(0), r(1), -v(2) if mn.startswith("sub") else v(2))])
                return [(mn, r(0), r(1), r(2))]
            if mn in ("sll", "srl", "sra"):
                return [(mn, r(0), r(1), v(2))]
            if mn in ("addi", "addiu", "andi", "ori", "xori", "slti", "sltiu"):
                return [(mn, r(0), r(1), v(2))]
            if mn == "lui":
                return [("lui", r(0), v(1))]
            if mn in ("lw", "sw", "lb", "lbu", "sb", "lh", "lhu", "sh"):
                m = re.match(r"^(.*)\((\$?\w+)\)$", ops[1].replace(" ", ""))
                if m:
                    off = self.value(m.group(1), n) if m.group(1) else 0
                    return [(mn, r(0), reg(m.group(2), n), off)]
                return fill([(mn, r(0), None, v(1))])     # label address: the simulator computes it
            if mn in ("beq", "bne"):
                if not ops[1].startswith("$"):
                    return [(mn + "i", r(0), v(1), v(2))]
                return [(mn, r(0), r(1), v(2))]
            if mn in ("blez", "bgtz", "bltz", "bgez", "beqz", "bnez"):
                return [(mn, r(0), v(1))]
            if mn in ("blt", "bgt", "ble", "bge", "bltu", "bgtu", "bleu", "bgeu"):
                b = ops[1]
                rb = reg(b, n) if b.startswith("$") else None
                return fill([(mn, r(0), rb, None if rb is not None else v(1), v(2))])
            if mn in ("j", "jal", "b"):
                return [(mn, v(0))]
            if mn == "jr":
                return [("jr", r(0))]
            if mn == "jalr":
                return [("jalr", 31 if len(ops) == 1 else r(0), r(len(ops) - 1))]
            if mn in ("mult", "multu", "div", "divu") and len(ops) == 2:
                return [(mn, r(0), r(1))]
            if mn in ("mul", "div", "divu", "rem", "remu") and len(ops) == 3:
                if ops[2].startswith("$"):
                    return fill([(mn + "3", r(0), r(1), r(2))])
                return fill([(mn + "3i", r(0), r(1), v(2))])
            if mn in ("mfhi", "mflo", "mthi", "mtlo"):
                return [(mn, r(0))]
            if mn == "li":
                return fill([("li", r(0), v(1))])
            if mn == "la":
                return fill([("li", r(0), v(1))])
            if mn == "move":
                return [("addu", r(0), r(1), 0)]
            if mn in ("neg", "negu"):
                return [("subu", r(0), 0, r(1))]
            if mn == "not":
                return [("nor", r(0), r(1), 0)]
            if mn == "abs":
                return fill([("abs", r(0), r(1))])
            if mn in ("seq", "sne", "sgt", "sge", "sle", "sgtu"):
                return fill([(mn, r(0), r(1), r(2))])
        except IndexError:
            raise AsmError(f"line {n}: {mn} is missing an operand")
        raise AsmError(f"line {n}: unsupported instruction {mn}")


class Machine:
    def __init__(self, prog, inp):
        self.p = prog
        self.r = [0] * 32
        self.hi = self.lo = 0
        self.r[28], self.r[29] = GP, SP
        self.mem = {}
        for i, b in enumerate(prog.data):
            self.mem[DATA + i] = b
        self.brk = DATA + len(prog.data) + ((-len(prog.data)) % 8)
        self.pc = prog.labels.get("main", TEXT)
        self.out = []
        self.inp = inp.split("\n") if inp else []
        self.done = False
        self.writes = []

    def ld(self, a, size, signed):
        if a % size:
            raise AsmError(f"unaligned {size}-byte load at 0x{a:08x}")
        v = int.from_bytes(bytes(self.mem.get(a + i, 0) for i in range(size)), "little")
        if signed and v & (1 << (8 * size - 1)):
            v -= 1 << (8 * size)
        return v

    def st(self, a, size, v):
        if a % size:
            raise AsmError(f"unaligned {size}-byte store at 0x{a:08x}")
        v &= (1 << (8 * size)) - 1
        for i, b in enumerate(v.to_bytes(size, "little")):
            self.mem[a + i] = b
        self.writes.append([a, size, v])

    def setr(self, i, v):
        if i:
            self.r[i] = v & M32

    def cstr(self, a):
        out = bytearray()
        while self.mem.get(a, 0) and len(out) < 10000:
            out.append(self.mem[a])
            a += 1
        return out.decode("latin-1")

    def syscall(self):
        v0, a0 = self.r[2], self.r[4]
        if v0 == 1:
            self.out.append(str(s32(a0)))
        elif v0 == 4:
            self.out.append(self.cstr(a0))
        elif v0 == 11:
            self.out.append(chr(a0 & 0xFF))
        elif v0 == 34:
            self.out.append(f"0x{a0:08x}")
        elif v0 == 35:
            self.out.append(f"{a0:032b}")
        elif v0 == 36:
            self.out.append(str(a0))
        elif v0 == 5:
            line = self.inp.pop(0) if self.inp else "0"
            try:
                self.setr(2, int(line.strip() or "0", 0))
            except ValueError:
                self.setr(2, 0)
        elif v0 == 12:
            line = self.inp.pop(0) if self.inp else "\n"
            self.setr(2, ord((line or "\n")[0]))
        elif v0 == 8:
            line = (self.inp.pop(0) if self.inp else "") + "\n"
            b = line.encode("latin-1", "replace")[: max(0, self.r[5] - 1)]
            for i, ch in enumerate(b + b"\0"):
                self.st(a0 + i, 1, ch)
        elif v0 == 9:
            self.setr(2, self.brk)
            self.brk += a0 + ((-a0) % 4)
        elif v0 in (10, 17):
            self.done = True
        else:
            raise AsmError(f"unsupported syscall {v0}")

    def step(self):
        if self.pc not in self.p.at:
            if self.pc == self.p.end:
                self.done = True        # fell off the end of the program (SPIM: same, with a warning)
                return None
            raise AsmError(f"jumped to 0x{self.pc:08x}, which holds no instruction")
        line, w, size = self.p.at[self.pc]
        pc = self.pc
        nxt = pc + size
        r, op = self.r, w[0]
        rv = lambda x: r[x] if x is not None else 0  # noqa: E731
        if op == "nop":
            pass
        elif op == "syscall":
            self.syscall()
        elif op in ("add", "addu"):
            self.setr(w[1], r[w[2]] + rv(w[3]))
        elif op in ("sub", "subu"):
            self.setr(w[1], rv(w[2]) - r[w[3]])
        elif op == "and":
            self.setr(w[1], r[w[2]] & r[w[3]])
        elif op == "or":
            self.setr(w[1], r[w[2]] | r[w[3]])
        elif op == "xor":
            self.setr(w[1], r[w[2]] ^ r[w[3]])
        elif op == "nor":
            self.setr(w[1], ~(r[w[2]] | rv(w[3])))
        elif op == "slt":
            self.setr(w[1], int(s32(r[w[2]]) < s32(r[w[3]])))
        elif op == "sltu":
            self.setr(w[1], int(r[w[2]] < r[w[3]]))
        elif op == "sll":
            self.setr(w[1], r[w[2]] << (w[3] & 31))
        elif op == "srl":
            self.setr(w[1], r[w[2]] >> (w[3] & 31))
        elif op == "sra":
            self.setr(w[1], s32(r[w[2]]) >> (w[3] & 31))
        elif op == "sllv":
            self.setr(w[1], r[w[2]] << (r[w[3]] & 31))
        elif op == "srlv":
            self.setr(w[1], r[w[2]] >> (r[w[3]] & 31))
        elif op == "srav":
            self.setr(w[1], s32(r[w[2]]) >> (r[w[3]] & 31))
        elif op in ("addi", "addiu"):
            self.setr(w[1], r[w[2]] + w[3])
        elif op == "andi":
            self.setr(w[1], r[w[2]] & (w[3] & 0xFFFF if w[3] >= 0 else w[3]))
        elif op == "ori":
            self.setr(w[1], r[w[2]] | (w[3] & 0xFFFF if 0 <= w[3] <= 0xFFFF else w[3]))
        elif op == "xori":
            self.setr(w[1], r[w[2]] ^ (w[3] & 0xFFFF if 0 <= w[3] <= 0xFFFF else w[3]))
        elif op == "slti":
            self.setr(w[1], int(s32(r[w[2]]) < w[3]))
        elif op == "sltiu":
            self.setr(w[1], int(r[w[2]] < (w[3] & M32)))
        elif op in ("sltui",):
            self.setr(w[1], int(r[w[2]] < (w[3] & M32)))
        elif op == "lui":
            self.setr(w[1], (w[2] & 0xFFFF) << 16)
        elif op == "li":
            self.setr(w[1], w[2])
        elif op in ("lw", "lh", "lhu", "lb", "lbu", "sw", "sh", "sb"):
            a = ((r[w[2]] if w[2] is not None else 0) + w[3]) & M32
            size = {"w": 4, "h": 2, "b": 1}[op[1]]
            if op[0] == "l":
                self.setr(w[1], self.ld(a, size, not op.endswith("u")))
            else:
                self.st(a, size, r[w[1]])
        elif op in ("beq", "bne", "beqi", "bnei"):
            b = r[w[2]] if op in ("beq", "bne") else w[2] & M32
            if (r[w[1]] == b) == (op[1] == "e"):
                nxt = w[3]
        elif op in ("blez", "bgtz", "bltz", "bgez", "beqz", "bnez"):
            x = s32(r[w[1]])
            if {"blez": x <= 0, "bgtz": x > 0, "bltz": x < 0, "bgez": x >= 0, "beqz": x == 0, "bnez": x != 0}[op]:
                nxt = w[2]
        elif op in ("blt", "bgt", "ble", "bge", "bltu", "bgtu", "bleu", "bgeu"):
            a = r[w[1]]
            b = r[w[2]] if w[2] is not None else w[3] & M32
            if not op.endswith("u"):
                a, b = s32(a), s32(b)
            if {"lt": a < b, "gt": a > b, "le": a <= b, "ge": a >= b}[op[1:3]]:
                nxt = w[4]
        elif op in ("j", "b"):
            nxt = w[1]
        elif op == "jal":
            self.setr(31, pc + 4)
            nxt = w[1]
        elif op == "jr":
            nxt = r[w[1]]
        elif op == "jalr":
            self.setr(w[1], pc + 4)
            nxt = r[w[2]]
        elif op in ("mult", "multu"):
            p = (s32(r[w[1]]) * s32(r[w[2]])) if op == "mult" else r[w[1]] * r[w[2]]
            self.lo, self.hi = p & M32, (p >> 32) & M32
        elif op in ("div", "divu"):
            a, b = (s32(r[w[1]]), s32(r[w[2]])) if op == "div" else (r[w[1]], r[w[2]])
            if b:
                q = int(a / b)
                self.lo, self.hi = q & M32, (a - q * b) & M32
        elif op in ("mul3", "mul3i"):
            self.setr(w[1], s32(r[w[2]]) * (s32(r[w[3]]) if op == "mul3" else w[3]))
        elif op in ("div3", "div3i", "rem3", "rem3i", "divu3", "divu3i", "remu3", "remu3i"):
            imm = op.endswith("i")
            if "u" in op[3:] or op.startswith(("divu", "remu")):
                a, b = r[w[2]], (r[w[3]] if not imm else w[3] & M32)      # unsigned
                if b == 0:
                    raise AsmError("division by zero")
                q = a // b
            else:
                a, b = s32(r[w[2]]), (s32(r[w[3]]) if not imm else w[3])
                if b == 0:
                    raise AsmError("division by zero")
                q = int(a / b)                                          # truncates toward zero, as MIPS does
            self.setr(w[1], q if op.startswith("div") else a - q * b)
        elif op == "mfhi":
            self.setr(w[1], self.hi)
        elif op == "mflo":
            self.setr(w[1], self.lo)
        elif op == "mthi":
            self.hi = r[w[1]]
        elif op == "mtlo":
            self.lo = r[w[1]]
        elif op == "abs":
            self.setr(w[1], abs(s32(r[w[2]])))
        elif op in ("seq", "sne", "sgt", "sge", "sle", "sgtu"):
            a, b = s32(r[w[2]]), s32(r[w[3]])
            self.setr(w[1], int({"seq": a == b, "sne": a != b, "sgt": a > b, "sge": a >= b, "sle": a <= b,
                                 "sgtu": r[w[2]] > r[w[3]]}[op]))
        else:
            raise AsmError(f"line {line}: cannot run {op}")
        self.pc = nxt & M32
        return line, pc


def ins_text(src_lines, line):
    t = strip_comment(src_lines[line - 1]).strip() if 0 < line <= len(src_lines) else ""
    return re.sub(r"^([A-Za-z_.$][\w.$]*)\s*:\s*", "", t)


def trace_source(src, inp="", max_steps=800):
    lines = src.split("\n")
    steps, error, truncated = [], None, False
    try:
        prog = Program(src)
    except AsmError as e:
        return {"version": 1, "kind": "mips", "language": "mips", "source": src, "steps": [], "stdout": "",
                "error": str(e), "truncated": False, "labels": {}, "data": {"base": DATA, "hex": ""}, "regs0": []}
    m = Machine(prog, inp)
    regs0 = m.r[:] + [m.hi, m.lo]
    prev = regs0[:]
    try:
        while not m.done:
            if len(steps) >= max_steps:
                truncated = True
                break
            m.writes = []
            res = m.step()
            if res is None:
                break
            line, pc = res
            now = m.r[:] + [m.hi, m.lo]
            steps.append({"line": line, "pc": pc, "ins": ins_text(lines, line),
                          "regs": {str(i): now[i] for i in range(34) if now[i] != prev[i]},
                          "mem": m.writes, "out": len("".join(m.out))})
            prev = now
    except AsmError as e:
        error = str(e)
    return {"version": 1, "kind": "mips", "language": "mips", "source": src, "steps": steps,
            "stdout": "".join(m.out), "error": error, "truncated": truncated,
            "labels": prog.labels, "data": {"base": DATA, "hex": bytes(prog.data).hex()}, "regs0": regs0}


def main():
    ap = argparse.ArgumentParser(description="Assemble and trace a MIPS program.")
    ap.add_argument("file")
    ap.add_argument("--max-steps", type=int, default=800)
    ap.add_argument("--input", default="")
    a = ap.parse_args()
    json.dump(trace_source(open(a.file, encoding="utf-8", errors="replace").read(), a.input, a.max_steps), sys.stdout)


if __name__ == "__main__":
    main()
