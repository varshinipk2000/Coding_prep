# Reverse words in a string (https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []

        for word in s.split():
            arr.append(word)

        res = ""

        for i in range(0,len(arr)):
            res = res + arr.pop() + " "

        return res[:len(res)-1]
