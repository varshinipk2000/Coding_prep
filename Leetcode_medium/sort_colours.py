# Sort Colours (https://leetcode.com/problems/sort-colors/description/)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n0 = n1 = n2 = 0
        for ele in nums:
            if ele==0:
                n0+=1
            elif ele==1:
                n1+=1
            else:
                n2+=1

        for i in range(0,len(nums)):
            if i <n0:
                nums[i] = 0
            elif i>=n0 and i<n0+n1:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums        
