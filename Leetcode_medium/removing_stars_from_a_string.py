# Removing stars from a string (https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75) 

class Solution:
    def removeStars(self, s: str) -> str:

        res = []

        for i in range(0,len(s)):
            if s[i]=='*':
                res.pop()
            else:
                res.append(s[i])

        return "".join(c for c in res)
