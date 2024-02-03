#Is subsequence (https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        if len(s)==0 and len(t)==0:
            return True

        subs = 0
        for i in range(0,len(t)):
            if subs<len(s) and s[subs]==t[i]:
                subs+=1

        if subs == len(s):
            return True
        return False
