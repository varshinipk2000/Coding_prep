# Counting bits (https://leetcode.com/problems/counting-bits/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def countBits(self, n: int) -> List[int]:

        if n==0:
            return [0]
        
        if n==1:
            return [0,1]
        
        result = [0,1]
        for i in range(2,n+1):
            num = i
            res = ""
            while num>=1:
                if num==1:
                    res = res+"1"
                    break
                else:
                    rem = num%2
                    num = math.floor(num/2)
                    res = res + str(rem)

            result.append(sum(int(e) for e in list(res)))
        
        return result      
