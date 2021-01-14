# In order to support adjustments, iterations and redesigns of this solver's method, it is first important
# to have a flexible system that can be used to represent boolean expressions.

# TODO: Works by setting a "required value" for each individual expression 

# Additionally, a parser to allow a string, eg: A & B to be converted to an expression in this data format is
# likely to help with the process.

class Expression:
    # Give it "Possible values" and "required value"

    # For variables, possible values is always both true and false
    # For other expressions, it is evaluateed recursively

    # Required value is the value required of the expression by its parent. For root epxression, this is just
    # TRUE (the goal of the problem). Might have values of TRUE and FALSE.

    # Will need to add "OR LInkage" to the equation. This is to evaulate both sides of an OR (Such that it
    # can be determined whether TRUE, FALSE or both are possible from an OR expression). This should probably
    # be done as a part of determining possible values of an OR expression (recursively evaluate both sides, 
    # in order to determine the possible values)
 
    pass

class Variable(Expression):
    pass

class ANDExpression(Expression):
    pass

class ORExpression(Expression):
    pass

class NOTExpression(Expression):
    pass
