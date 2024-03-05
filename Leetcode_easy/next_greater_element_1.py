# Next Greater Element 1 (https://leetcode.com/problems/next-greater-element-i/description/)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = deque()
        res = [-1]*len(nums2)

        for i in range(len(nums2)-1,-1,-1):
            
            while stack and stack[-1]<=nums2[i]:
                stack.pop()

            if len(stack)==0:
                res[i] = -1
            else:
                res[i] = stack[-1]
            stack.append(nums2[i])

        finres = []
        for i in range(0,len(nums1)):
            pos = nums2.index(nums1[i])
            finres.append(res[pos])

        return finres       
