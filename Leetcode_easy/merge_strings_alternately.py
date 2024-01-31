# Merge strings alternately (https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        word = ""
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                word = word+word1[i]
            if i<len(word2):
                word = word+word2[i]
            i = i+1
        
        return word
