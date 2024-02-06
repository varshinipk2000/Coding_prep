# single number (https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        for i in range(0, len(nums)):
            if i==0:
                if nums[i] not in nums[i+1:]:
                    return nums[i]
            elif i==len(nums)-1:
                if nums[i] not in nums[0:i-1]:
                    return nums[i]
            else:
                if((nums[i] not in nums[0:i]) and (nums[i] not in nums[i+1:len(nums)])):
                    return nums[i]
