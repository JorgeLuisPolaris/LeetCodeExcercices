"""
Given n pairs of parentheses, write a function 
to generate all combinations of well-formed parentheses.
"""
from typing import List


def generateParenthesis(n: int) -> List[str]:
    stack = []
    res = []
    def gen(left, right):
        if left==right==n:
            res.append("".join(stack))
            return
        if left<n:
            stack.append("(")
            gen(left+1,right)
            stack.pop()
        if left>right:
            stack.append(")")
            gen(left,right+1)
            stack.pop()
    gen(0,0)
    return res
print(generateParenthesis(4))