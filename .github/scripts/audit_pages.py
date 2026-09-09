#!/usr/bin/env python3
"""Catch the three site problems that a Jekyll build will not shout about.

Run from the repository root:

    python3 .github/scripts/audit_pages.py

Exits non-zero and prints every finding if anything is wrong.

1.  Liquid that was meant as literal text.  Jekyll runs Liquid over every page
    under _pages before Markdown ever sees it, whether or not the file has front
    matter, and an inline code span does not protect anything.  A stray
    {{ user.name }} in prose is valid Liquid for a variable that does not exist,
    so it renders as the empty string with no warning at all: the words simply
    vanish from the published page.  Literal braces belong inside {% raw %}, or,
    in the Activity decks, built by string concatenation (see 3).

2.  A layout that does not exist.  Jekyll warns once and then renders the page
    with no template at all: no stylesheet, no navigation, no title.  The build
    still succeeds and still deploys, so this is easy to miss.

3.  Single-dollar inline math.  MathJax 3 does not treat $...$ as a delimiter, so
    such a span publishes as raw LaTeX in the middle of a sentence.  kramdown turns
    $$...$$ into \\(...\\) even mid-sentence, which MathJax does render, and which is
    what the rest of the repository uses.  LiaScript decks have their own renderer
    and are exempt.

4.  Liquid of any kind in _pages/Activities.  Those files are LiaScript decks,
    served raw to the viewer from the branch as well as rendered by Jekyll, so
    neither escape works: bare braces break the Jekyll build, and {% raw %} tags
    show up literally inside the Python in the viewer.  The only safe state is
    no Liquid at all, with literal braces assembled by concatenation:

        print("  start: " + "{" + ", ".join(names) + "}")
"""

import glob
import os
import re
import sys

PAGES = "_pages"
LAYOUTS = "_layouts"
DECKS = os.path.join(PAGES, "Activities")

RAW_BLOCK = re.compile(r"\{%\s*raw\s*%\}.*?\{%\s*endraw\s*%\}", re.S)
LIQUID = re.compile(r"\{\{(.*?)\}\}|\{%(.*?)%\}", re.S)
OPENER = re.compile(r"\{\{|\{%")
FENCE = re.compile(r"\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
FRONT_MATTER_LAYOUT = re.compile(r"^layout:[ \t]*([^\r\n]+)", re.M)
DOLLAR_MATH = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)")
# A TeX command, an escaped space (the "\ " spacing idiom), a sub/superscript, a
# bracketed variable, or an equation: all math, and none of it ordinary prose.
TEX = re.compile(r"\\[a-zA-Z]+|\\[\s(){}\[\]\\]|[_^]\{|\[[A-Za-z]\]|^[^A-Za-z]*[A-Za-z][^=]*=[^=]")

# Variables the site actually defines, and the tags Liquid actually has.
KNOWN_VARS = re.compile(r"^\s*(site\.|page\.|content\b|include\.|paginator\.|forloop\.)")
KNOWN_TAGS = re.compile(
    r"^\s*(if|elsif|else|endif|for|endfor|assign|capture|endcapture|unless|endunless"
    r"|case|when|endcase|comment|endcomment|seo|include|highlight|endhighlight"
    r"|raw|endraw|break|continue|cycle|tablerow|endtablerow)\b"
)


def line_of(text, index):
    return text[:index].count("\n") + 1


def pages():
    return sorted(glob.glob(os.path.join(PAGES, "**", "*.md"), recursive=True))


def blank_raw_blocks(source):
    """Replace {% raw %}...{% endraw %} with spaces, keeping every offset intact."""
    return RAW_BLOCK.sub(lambda m: " " * len(m.group(0)), source)


def liquid_all_defined(text):
    """True when every Liquid expression in text is one the site actually defines.

    A defined variable inside backticks renders its value, which is what the page
    wants: `{{ page.info.coursenum }}` publishes as `CS173`. Only Liquid that
    resolves to nothing is a problem there, and check_liquid already reports that
    separately as "undefined Liquid".
    """
    for match in LIQUID.finditer(text):
        is_variable = match.group(1) is not None
        inner = match.group(1) if is_variable else match.group(2)
        if not (KNOWN_VARS.match(inner) if is_variable else KNOWN_TAGS.match(inner)):
            return False
    return not OPENER.search(LIQUID.sub("", text))


def check_liquid(findings):
    for path in pages():
        source = open(path, encoding="utf-8", errors="replace").read()
        body = blank_raw_blocks(source)

        for match in LIQUID.finditer(body):
            is_variable = match.group(1) is not None
            inner = match.group(1) if is_variable else match.group(2)
            known = KNOWN_VARS.match(inner) if is_variable else KNOWN_TAGS.match(inner)
            if not known:
                findings.append((
                    path, line_of(body, match.start()), "undefined Liquid",
                    match.group(0)[:70].replace("\n", "\\n"),
                    "Liquid will render this as nothing. Wrap it in {% raw %} if it is literal text.",
                ))

        # An opener with no closer anywhere: Liquid aborts the build on these.
        leftover = LIQUID.sub("", body)
        for match in OPENER.finditer(leftover):
            findings.append((
                path, line_of(leftover, match.start()), "unclosed Liquid",
                match.group(0), "No matching closing tag.",
            ))

        # Liquid inside code is nearly always meant to be shown, not evaluated.
        in_fence = False
        for number, line in enumerate(body.split("\n"), start=1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if not OPENER.search(line):
                continue
            if in_fence:
                findings.append((
                    path, number, "Liquid in a code fence", line.strip()[:70],
                    "Code fences do not protect Liquid. Wrap the fence in {% raw %}.",
                ))
            else:
                for span in INLINE_CODE.finditer(line):
                    if OPENER.search(span.group(0)) and not liquid_all_defined(span.group(0)):
                        findings.append((
                            path, number, "Liquid in an inline code span", span.group(0)[:70],
                            "Backticks do not protect Liquid. Wrap it in {% raw %}.",
                        ))


def check_dollar_math(findings):
    for path in pages():
        if path.startswith(DECKS + os.sep):
            continue        # LiaScript renders $...$ itself
        source = open(path, encoding="utf-8", errors="replace").read()
        in_fence = False
        for number, line in enumerate(source.split("\n"), start=1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence or "$" not in line:
                continue
            masked = INLINE_CODE.sub(lambda m: " " * len(m.group(0)), line)
            for match in DOLLAR_MATH.finditer(masked):
                if not TEX.search(match.group(1)):
                    continue
                findings.append((
                    path, number, "single-dollar inline math",
                    match.group(0)[:70],
                    "MathJax 3 will not render this; it publishes as raw LaTeX. Use $$...$$.",
                ))


def check_layouts(findings):
    for path in pages():
        source = open(path, encoding="utf-8", errors="replace").read()
        if not source.startswith("---"):
            continue
        match = FRONT_MATTER_LAYOUT.search(source)
        if not match:
            continue
        name = match.group(1).strip().strip("\"'")
        if not os.path.isfile(os.path.join(LAYOUTS, name + ".html")):
            available = sorted(
                os.path.basename(p)[:-5] for p in glob.glob(os.path.join(LAYOUTS, "*.html"))
            )
            findings.append((
                path, line_of(source, match.start()), "missing layout", name,
                "Jekyll renders the page with no template. Available: " + ", ".join(available),
            ))


def check_decks(findings):
    for path in sorted(glob.glob(os.path.join(DECKS, "*.md"))):
        source = open(path, encoding="utf-8", errors="replace").read()
        for match in OPENER.finditer(source):
            findings.append((
                path, line_of(source, match.start()), "Liquid in a LiaScript deck",
                source[match.start():match.start() + 60].split("\n")[0],
                "Decks are served raw to the viewer, so {% raw %} would show literally. "
                "Build literal braces by concatenation instead.",
            ))


def main():
    if not os.path.isdir(PAGES):
        print(f"error: run this from the repository root ({PAGES}/ not found)")
        return 2

    findings = []
    check_liquid(findings)
    check_dollar_math(findings)
    check_layouts(findings)
    check_decks(findings)

    checked = len(pages())
    if not findings:
        print(f"audit_pages: {checked} pages checked, nothing to report.")
        return 0

    print(f"audit_pages: {checked} pages checked, {len(findings)} finding(s).\n")
    for path, number, kind, snippet, hint in findings:
        print(f"{path}:{number}: {kind}")
        print(f"    {snippet}")
        print(f"    {hint}\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
