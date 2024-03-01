# Find the duplicate number (https://leetcode.com/problems/find-the-duplicate-number/description/)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}

        for ele in nums:
            if ele in map:
                return ele
            else:
                map[ele] = 1

        return 0
