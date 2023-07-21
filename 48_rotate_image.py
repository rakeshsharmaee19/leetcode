## Solution 1
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)-1):
            for j in range(i+1, len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


## Solution 2
import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a=np.array(matrix)
        m=np.rot90(a,3)
        b=[]
        for i in m:
            b.append(i)
        matrix.clear()
        matrix.extend(b)
