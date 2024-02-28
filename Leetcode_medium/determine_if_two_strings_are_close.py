# Determine if two strings are close (https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1)!=len(word2):
            return False
        
        map1 = {}
        map2 = {}

        for i in range(0,len(word1)):
            if word1[i] in map1:
                map1[word1[i]]+=1
            else:
                map1[word1[i]] = 1

        for i in range(0,len(word2)):
            if word2[i] in map2:
                map2[word2[i]]+=1
            else:
                map2[word2[i]] = 1

        if map1==map2:
            return True

        v1 = list(map1.values())
        v2 = list(map2.values())
        k1 = list(map1.keys())
        k2 = list(map2.keys())

        k1.sort()
        k2.sort()
        v1.sort()
        v2.sort()

        if v1==v2 and k1==k2:
            return True

        return False 
