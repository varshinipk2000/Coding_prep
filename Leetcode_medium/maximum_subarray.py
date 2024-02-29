# Maximum Subarray (https://leetcode.com/problems/maximum-subarray/)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        s = 0
        maxsum = -100000

        for ele in nums:
            s+=ele

            maxsum = max(maxsum, s)

            if s<0:
                s = 0

        return maxsum       
