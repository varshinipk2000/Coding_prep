# Search a 2D matrix (https://leetcode.com/problems/search-a-2d-matrix/description/)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """for row in matrix:
            if target in row:
                return True

        return False  """      

        m = len(matrix)
        n = len(matrix[0])

        if m==1 and n==1:
            return target==matrix[0][0]

        searchlist = []
        for row in matrix:
            if target>=row[0] and target<=row[n-1]:
                searchlist[:] = row

        if len(searchlist)==0:
            return False

        l = 0
        r = n-1

        while l<=r:
            mid = (l+r)//2
            if target<searchlist[mid]:
                r = mid-1
            elif target>searchlist[mid]:
                l = mid+1
            else:
                return True

        return False
