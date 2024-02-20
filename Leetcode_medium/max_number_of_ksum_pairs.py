# Max Number of K-sum pairs (https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        c = 0
        nums.sort()

        while left<right:
            s = nums[left]+nums[right]

            if s>k:
                right-=1
            elif s<k:
                left+=1
            else:
                c+=1
                left+=1
                right-=1

        return c         
