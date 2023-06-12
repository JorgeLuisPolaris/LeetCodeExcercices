from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        #se obtienen los valores de las filas y columnas.
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1 
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if (top > bot): 
            """
            en caso de que el top sea más grande que el bot significa que el valor target
            es más grande que el valor más grande de la matriz o más chico que el valor
            más chico por lo que regresamos false
            """
            return False
        #cuando ya se sabe en qué fila esta simplemente se realiza un binary search normal
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(searchMatrix(matrix,target))