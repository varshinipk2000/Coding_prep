"""Kids with the greatest number of candies (https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75)
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = candies[0]

        for i in range(1,len(candies)):
            maxcandies = max(maxcandies,candies[i])

        result = [] 
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= maxcandies:
                #result[i] = True
                result.append(True)
            else:
                #result[i] = False
                result.append(False)

        return result
        
