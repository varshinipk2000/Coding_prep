# (643. Maximum Average Subarray I) https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k==1:
            return max(nums)

        if k==len(nums):
            return sum(nums)/k

        ksum = sum(nums[0:k])
        avg = ksum/k
        i=0
        while i+k<len(nums):
            ksum = ksum + nums[i+k] - nums[i]
            avg = max(avg, ksum/k)
            i+=1

        return avg        
