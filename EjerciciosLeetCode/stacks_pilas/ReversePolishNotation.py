"""
You are given an array of strings tokens that represents an arithmetic expression 
in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents 
the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
"""

from typing import List


def evalRPN(tokens: List[str]) -> int:
    numeros = []
    operadores = ['-','+','*','/']
    for token in tokens:
        if token not in operadores:
            numeros.append(int(token))
            print(numeros)
        else:
            n1 = numeros.pop()
            n2= numeros.pop()
            if token == '+':
                numeros.append(n2+n1)
            elif token == '/':
                numeros.append(int(n2/n1))
            elif token == '*':
                numeros.append(n2*n1)
            elif token == '-':
                numeros.append(n2-n1)
            print(numeros)

    print(numeros)
    return numeros[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evalRPN(tokens)