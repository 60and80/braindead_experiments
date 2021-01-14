## README

With this project, I wanted to have an attempt at solving the BSP (Boolean Satisfiability Problem), which
is an NP hard mathematics/computer science problem. The problem is to find an algorithm that can evaluate
any boolean expression with arbitrary variables, and determine whether there is an input that causes the
expression to evaluate to true. Eg, the expression:

A & B

Will evaluate to true iff the input A and input B are both set to true.

A   B   A&B
0   0   0
1   0   0
0   1   0
1   1   1

The goal is to try and develop an algorithm that solves in quadratic time, rather than exponential, even for
worst-case scenario problems. Note that I am not convinced I can succeed in this - but I am also not sure why
it is a difficult problem. The goal is to investigate the problem, and attempt to find a solution.

Note: The goal is not to determine what the solution is, just whether one exists. I can sort this out later if I want.

I will be doing no research into current knowledge and methods of solving this problem. This is both to avoid colouring my assumptions about the problem, and because I want to figure out methods for myself (even if they already exist)