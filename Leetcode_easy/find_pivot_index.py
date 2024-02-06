# Find pivot index (https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        l = 0
        r = sum(nums[1:len(nums)])
        if l==r:
            return 0

        for pi in range(1,len(nums)):
            l+=nums[pi-1]
            r-=nums[pi]
            if l==r:
                return pi

        return -1


        
