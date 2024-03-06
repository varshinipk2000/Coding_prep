# Rotting Oranges (https://leetcode.com/problems/rotting-oranges/description/)

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()


        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        time = 0

        while q and fresh>0:
            
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    row = dr+r
                    col = dc+c

                    if row<0 or row==m or col<0 or col==n or grid[row][col]!=1:
                        continue

                    grid[row][col] = 2
                    q.append([row,col])
                    fresh-=1
                
            time+=1

        if fresh==0:
            return time
        else:
            return -1
