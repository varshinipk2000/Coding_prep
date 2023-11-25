#Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)
class Solution: 
  def containsDuplicate(self, nums: List[int]) -> bool: 
    count_set = set() 
    for ele in nums: 
      count_set.add(ele) 

    if(len(count_set)<len(nums)): 
      return True 
    return False
