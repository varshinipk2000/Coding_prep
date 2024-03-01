# Majority Element (https://leetcode.com/problems/majority-element/description/)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num] = 1

        for k,v in hashmap.items():
            if v>(len(nums)//2):
                return k

        return 0      
