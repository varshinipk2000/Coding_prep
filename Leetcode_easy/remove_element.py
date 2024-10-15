# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        while val in nums:
            c+=1
            nums.remove(val)

        for i in range(c):
            nums.append(val)

        return len(nums)-c     
