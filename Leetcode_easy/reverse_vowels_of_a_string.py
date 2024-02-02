#Reverse vowels of a string (https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)==1:
            return s

        left = 0
        right = len(s) - 1

        strlist = list(s)
        vowels = "aeiouAEIOU"

        while left<right:

            while left < right and strlist[left] not in vowels:
                left+=1

            while left<right and strlist[right] not in vowels:
                right-=1

            temp = strlist[left]
            strlist[left] = strlist[right]
            strlist[right] = temp
            left+=1
            right -=1

        return "".join(strlist)

