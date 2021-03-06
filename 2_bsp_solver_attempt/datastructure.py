# In order to support adjustments, iterations and redesigns of this solver's method, it is first important
# to have a flexible system that can be used to represent boolean expressions.

# toDONE: Works by setting a "required value" for each individual expression 
# TODO: Research Python strong typing
# TODO: Formalise documentation
# TODO: FIGURE OUT HOW TO Attach variable values to possible values
# TODO: Error handling! Especially for truthTable class
# TODO: Test

# Additionally, a parser to allow a string, eg: A & B to be converted to an expression in this data format is
# likely to help with the process.
# # Give it "Possible values" and "required value"

# For variables, possible values is always both true and false
# For other expressions, it is evaluateed recursively

# Required value is the value required of the expression by its parent. For root epxression, this is just
# TRUE (the goal of the problem). Might have values of TRUE and FALSE.

# Will need to add "OR LInkage" to the equation. This is to evaulate both sides of an OR (Such that it
# can be determined whether TRUE, FALSE or both are possible from an OR expression). This should probably
# be done as a part of determining possible values of an OR expression (recursively evaluate both sides, 
# in order to determine the possible values)

# How to link different instances of the same variable??
# Requirements: 
# Have a data structure requiring that A == A elsewhere in the equation, at all times
# In parsing, automatically detect multiple instances of the same variable, and link them
# Efficient ways to link A <-> A, B <-> B, within a structure that evaluates recursively like this one?

# Ok I think much more sensible:
# As part of recursive structure, pass up truth table of all values involved thus far, mapped to output 
# of the expression as evaluated so far. So, (A | B) & A would evaluate like this:

# A  B  A|B  (A|B) & A
# 0  0  0       0
# 1  0  1       1
# 0  1  1       0
# 1  1  1       1

# This way the system can immediately eliminate combinations where there are conflicting 
# This method would also have to keep track of which values were already included - such that if another
# instance of the A variable is encountered, it is aliased to the existing one. This can be done by linking
# all instances of the variable at parsing time.

# At this point I think I am starting to understand why this is an NP hard problem. This design thus far
# is just a fairly standard pen and paper algorithm for solving small boolean problems.

# Quick and dirty solution would be to eliminate possibilities where A != A as a part of evaluation?

class Expression:
    
    required_val = True
    possible_vals = [True, False]
    
    def __init__(self, req_val):
        self.required_val = req_val

    def evaluate(self): # Important for evaluating entire tree structure TODO: Add variable pulling
        return self.required_val in self.possible_vals
 
class Variable(Expression):
    possible_vals = [True, False]

class ANDExpression(Expression):
    child1 = None 
    child2 = None

    def __init__(self, req_val, expr1, expr2):
        self.required_val = req_val
        self.child1 = expr1
        self.child2 = expr2
        self.possible_vals = []
        if True in self.child1.possible_vals & True in self.child2.possible_vals: # TODO: Refactor this!!
            self.possible_vals.append(True)
        if False in self.child1.possible_vals | False in self.child2.possible_vals:
            self.possible_vals.append(False)


class ORExpression(Expression):
    child1 = None
    child2 = None

    def __init__(self, req_val, expr1, expr2):
        self.required_val = req_val
        self.child1 = expr1
        self.child2 = expr2
        self.possible_vals = []
        if True in self.child1.possible_vals | True in self.child2.possible_vals:
            self.possible_vals.append(True)
        if False in self.child1.possible_vals & False in self.child2.possible_vals:
            self.possible_vals.append(False)


class NOTExpression(Expression):
    child = None

    def __init__(self, req_val, expr):
        self.required_val = req_val
        self.child = expr
        self.possible_vals = []
        if False in self.child.possible_vals:
            self.possible_vals.append(True)
        if True in self.child.possible_vals:
            self.possible_vals.append(False)

class TruthTable: # Adding this just turns this into a BF exponential approach.
    varList = None
    truthTable = None

    def __init__(self, varList, outputList):
        self.varList = varList
        self.truthTable = []
        for i in range(2 ** len(varList)): # EXPONENTIAL! Oop. Try Hashing?
            entry = []
            for j in range(len(varList)):
                entry.append(i % (j+1 * 2) == 1) # 0 false, 1 true
            self.truthTable.append(entry)
            

# SHELVING for now - "possible vals" approach has a major flaw, in that it does not actually account for
# multiple instances of the same variable. Can see no obvious way to fix - making another attempt at 
# framework. 