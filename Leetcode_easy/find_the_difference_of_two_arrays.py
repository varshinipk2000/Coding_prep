#Find the difference of two arrays (https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        arr1 = []
        arr2 = []
        result = []

        for i in range(0,len(nums1)):
            if nums1[i] not in nums2:
                arr1.append(nums1[i])

        for i in range(0,len(nums2)):
            if nums2[i] not in nums1:
                arr2.append(nums2[i])

        result.append(set(arr1))
        result.append(set(arr2))

        return result       
