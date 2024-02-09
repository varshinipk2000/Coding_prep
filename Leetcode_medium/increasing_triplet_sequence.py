# Increasing triplet sequence (https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        if len(nums)<=2:
            return False

        min1 = min2 = 2150000000
        for num in nums:
            if num<=min1:
                min1 = num
            elif num<=min2:
                min2 = num
            else:
                return True

        return False
