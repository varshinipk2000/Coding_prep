# pow(x,n) (https://leetcode.com/problems/powx-n/)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """if n==0:
            return 1
        return x**n   """   

        if n==0:
            return 1
        elif n<0:
            return 1/(x*self.myPow(x,-n-1))
        elif n%2==0:
            num = self.myPow(x,n//2)
            return num*num
        else:
            return x*self.myPow(x,n-1)        
