Move Zeroes (https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i in range(0,len(nums)): #loop to count zeroes
            if nums[i]==0:
                c+=1

        temp_c = c

        while c>0:
            nums.remove(0)
            c-=1

        while temp_c>0:
            nums.append(0)
            temp_c-=1

        return nums
