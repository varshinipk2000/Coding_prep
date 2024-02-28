# Pascals Triangle (https://leetcode.com/problems/pascals-triangle/)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]

        def getlist(l):
            temp = []
            temp.append(1)
            for i in range(len(l)-1):
                s = l[i]+l[i+1]
                temp.append(s)
            temp.append(1)
            return temp
        
        n = 2
        res = [[1],[1,1]]
        temp = [1,1]

        while n<numRows:
            temp = getlist(temp)
            res.append(temp)
            n+=1
        
        return res       
