# 2-SAT-Solver
A 2-sat solver class written in python. Expressions are passed an init parameter to CNF class. The format of the expression is similar to a regular boolean expression, except the variables are format strings ("{0}") where each different number represents a different variable.

# Example
```
from cnf import CNF

expr = '({0} or {1}) and ({1} or {0}) and ({0} or {1})'
cnf = CNF(expr)

# Check if any combination of inputs satisfies expression
print(cnf.check()) # "(0, 1)"

# Evaluate expression with input (0, 1)
print(cnf.eval((0, 1)) # "1"
```
