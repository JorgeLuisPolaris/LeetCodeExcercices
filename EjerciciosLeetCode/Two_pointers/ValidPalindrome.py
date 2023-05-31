"""
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include
 letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

import re

def isPalindrome(s: str) -> bool:
    texto= str.lower(re.sub(r'[^a-zA-Z0-9]', '', s))
    n = len(texto)
    print(texto)
    for i in range(n):
        if texto[i]!= texto[n-1-i]:
            return False 
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))