#Valid Anagram (https://leetcode.com/problems/valid-anagram/description/)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for i in range(0,len(s)):
            s1.append(s[i])
            #Instead of this loop to create s1 and s2 list and then sorting, you can directly use sorted(s) and sorted(t)
        
        for i in range(0,len(t)):
            s2.append(t[i])

        s1.sort()
        s2.sort()

        if s1==s2:
            return True
        return False
