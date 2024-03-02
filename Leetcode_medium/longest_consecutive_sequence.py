# Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence/)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)<1:
            return 0

        nums.sort()
        lastnum = -10000000000
        maxc = 0
        c = 1
        for num in nums:
            if lastnum+1==num:
                c+=1
                lastnum = num
            elif lastnum==num:
                continue
            else:
                lastnum = num
                c = 1  
            maxc = max(maxc,c)
        return maxc
