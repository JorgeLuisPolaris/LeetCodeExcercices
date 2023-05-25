"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.

 """
from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for palabra in strs:
        letras = [0] * 26
        for letra in palabra:
            letras[ord(letra) - ord("a")] += 1
        res[tuple(letras)].append(palabra)
    return list(res.values())

ejemplo = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(ejemplo))