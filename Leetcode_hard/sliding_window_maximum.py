# Sliding Window Maximum (https://leetcode.com/problems/sliding-window-maximum/description/)

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        n = len(nums)
        res = []
        
        for i in range(k):
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
        res.append(nums[d[0]])

        for i in range(k,n):
            if i-d[0] >= k :
                d.popleft()
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            res.append(nums[d[0]])
        return res
