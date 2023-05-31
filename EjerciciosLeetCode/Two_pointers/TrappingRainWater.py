"""
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.
"""
from typing import List


def trap(height: List[int]) -> int:
    res, izquierda, derecha = 0, 0, len(height)-1
    maxAlturaIzquierda, maxAlturaDerecha = height[izquierda], height[derecha]
    while izquierda<derecha:
        if maxAlturaIzquierda<maxAlturaDerecha:
            izquierda+=1
            maxAlturaIzquierda = maxAlturaIzquierda if maxAlturaIzquierda> height[izquierda] else height[izquierda]
            res+= maxAlturaIzquierda- height[izquierda]
        else:
            derecha-=1
            maxAlturaDerecha = maxAlturaDerecha if maxAlturaDerecha> height[derecha] else height[derecha]
            res+=maxAlturaDerecha- height[derecha]  
    return res

height = [4,2,0,3,2,5]

print(trap(height))