#Max vowels in a substring of given length (https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        substring = s[:k]
        vowels = "aeiou"
        maxc = 0
        for i in range(0,k):
            if substring[i] in vowels:
                maxc+=1
        c = maxc

        for i in range(0, len(s)-k):
            c += (s[k+i] in vowels) - (s[i] in vowels)
            maxc = max(c, maxc)

        return maxc        
