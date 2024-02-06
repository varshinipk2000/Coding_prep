# Nth tribonacci number (https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1

        t = [0,1,1]
        for i in range(3,n+1):
            t.append(sum(t[i-3:i]))

        return t.pop()      
