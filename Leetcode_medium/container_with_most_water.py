# Container with most water (https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right])* (right - left)
            maxarea = max(maxarea, area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxarea        
