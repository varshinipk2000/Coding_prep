#Find the highest altitude (https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curralt = maxalt = 0

        for i in range(0,len(gain)):
            curralt = curralt + gain[i]
            maxalt = max(curralt, maxalt)

        return maxalt
        
