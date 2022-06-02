'''
cnf.py

Defines a class for representing CNF expressions,
evaluating them, and checking if they are satisfiable.

Author: Jacob Sanders
'''
import re

class CNF:
    '''
    Defines a CNF expression, a method for evaluating
    that expression with a provided set of values,
    and a function which checks if any combination of
    inputs satisfy the expression (evaluates to '1'/'True')
    '''
    def __init__(self, expr):
        '''
        Initialize CNF with provided expr and define
        'n' to represent how many variables are in the
        expression.
        '''
        self._expr = expr
        self._n = len(set(re.findall(r'{[\d]}', expr)))
    
    def eval(self, vals):
        '''
        Evaluate the expression with the provided boolean
        values for each variable.
        '''
        return eval(self._expr.format(*vals))
     
    def check(self):
        '''
        Exhaustively check the result of evaluating the
        expression with every different combination of
        boolean values for each variable.
        
        If satisfying input is found, return the values
        that satisfied the expression as a tuple of ints
        [0-1].
        
        If no satisfying input is found, return None.
        '''
        for i in range(2**self._n):
            vals = tuple(bin(i)[2:].zfill(self._n))
            if self.eval(vals):
                return tuple(map(int, vals))
        return None

if __name__ == '__main__':
  '''
  Example and test case.
  '''
  expr = '({0} or {1}) and ({1} or {0}) and ({0} or {1})'
  cnf = CNF(expr)
  # Ensure that number of variables is evaluated properly
  assert(cnf._n == 2)
  # Ensure that evaluation functions properly
  assert(cnf.eval((0, 1)) == 1)
  # Ensure that check finds solution
  assert(cnf.check() == (0, 1))
