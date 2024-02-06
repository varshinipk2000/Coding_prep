#Maximum Average Subarray 1 (https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==len(nums):
            return sum(nums)/k

        currsum = maxsum = sum(nums[0:k])

        for i in range(k, len(nums)):
            currsum = currsum + nums[i] - nums[i-k]

            maxsum = max(maxsum, currsum)

        return maxsum/k
