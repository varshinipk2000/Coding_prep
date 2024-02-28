# Equal row and column pairs (https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = {}
        col = {}

        i=0
        for l in grid:
            row[i] = l
            i+=1
        
        n = len(grid[0])

        for i in range(0,n):
            templist = []
            for j in range(0,n):
                templist.append(grid[j][i])
            col[i] = templist

        l1 = list(row.values())
        l2 = list(col.values())

        res = 0
        for l in l1:
            for m in l2:
                if l==m:
                    res+=1

        return res         
