---
layout: exercise_horstmann
permalink: /Modules/Horstmann/Swap/Exercise
title: "CS173: Intro to Computer Science - Horstmann Parsons Puzzle: Swap"
excerpt: "CS173: Intro to Computer Science - Horstmann Parsons Puzzle: Swap"

info:
  points: 0
  instructions: "Fill in the prompts to trace the algorithm and swap two <code>int</code> variables."
  goals:
    - To manipulate variables by correctly swapping their values
  
exercisecode: |
    if (state === undefined) { 
      state = {}
      state.a = sim.randInt(0, 9)
      if (state.a == 8) state.a = 10
    }

    const code = sim.add(0, 0, new Code(`
    int a = ${state.a};
    int b = 8;
    int temp = a;
    a = b;
    b = temp;
    `))
    const vars = sim.add(0, 3, new Frame())
    yield sim.start(state)

    vars.a = state.a
    yield sim.next('Initialized a') // Wait for the student to hit the Next button
    code.go(2) 
    vars.b = 8
    yield sim.next('Initialized b')
    code.go(3)
    vars.temp = yield sim.ask(vars.a)
    code.go(4)
    vars.a = yield sim.ask(vars.b)
    code.go(5)
    vars.b = yield sim.ask(vars.temp)
        
---
