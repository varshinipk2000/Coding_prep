# Rotate Matrix (https://leetcode.com/problems/rotate-image/description/)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """m = len(matrix)
        #res = [[]]*m
        res = []

        for j in range(0,m):
            temp = []
            for i in range(m-1,-1,-1):
                temp.append(matrix[i][j])
            res.append(temp)

        matrix[:] = res"""

        m = len(matrix)
        
        for i in range(0,m):
            for j in range(i+1,m):
                if i!=j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        for row in matrix:
            start = 0
            end = m-1
            while start<end:
                temp = row[start]
                row[start] = row[end]
                row[end] = temp
                start+=1
                end-=1        
