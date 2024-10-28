#Move Zeroes (https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for ele in nums:
            if ele ==0:
                count+=1

        while(count):
            nums.remove(0)
            nums.append(0)
            count-=1     
