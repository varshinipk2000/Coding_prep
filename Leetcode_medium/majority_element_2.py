# Majority Element 2 (https://leetcode.com/problems/majority-element-ii/description/)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num] = 1
        res = []
        for k,v in hashmap.items():
            if v>(len(nums)//3):
                res.append(k)

        return res  
