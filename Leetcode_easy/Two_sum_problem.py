# Two Sum Problem (https://leetcode.com/problems/two-sum/description/)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force

        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

        #optimized
        mydict = {}
        for i in range(0,len(nums)):
            mydict[nums[i]] = i
        
        for i in range(0, len(nums)):
            num2 = target - nums[i]
            if num2 in mydict.keys() and mydict[num2]!=i:
                return [i, mydict[num2]]

        return []
