# Guess the number - Higher or lower (https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if n==1:
            result = guess(n)
            if result == 0:
                return n

        l = 1
        r = n

        while l<r:
            mid = (l+r)/2
            guessapi = guess(mid)
            if guessapi == -1:
                r = mid
            elif guessapi == 1:
                l = mid
            else:
                return int(mid)      
