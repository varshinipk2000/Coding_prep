# Product of array except self (https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        p = 1
        zero_count = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                p = p*nums[i]
            else:
                zero_count+=1

        if zero_count >1 :
            return [0]*len(nums)
        if 0 in nums:
            for i in range(0,len(nums)):
                if nums[i]!=0:
                    result.append(0)
                else:
                    result.append(p)
        else:
            for i in range(0,len(nums)):
                result.append(int(p/nums[i]))

        return result      
