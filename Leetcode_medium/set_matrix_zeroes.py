# Set matrix zeroes ()

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        rz = [False]*m
        cz = [False]*n

        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    rz[row] = True
                    cz[col] = True

        for row in range(m):
            for col in range(n):
                if rz[row] or cz[col]:
                    matrix[row][col] = 0

        return matrix 
