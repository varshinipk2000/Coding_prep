#Unique Number of occurences (https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        if len(arr)==1:
            return True
        
        map ={}

        for i in range(0,len(arr)):
            if arr[i] in map:
                map[arr[i]]+=1
            else:
                map[arr[i]] = 1

        values = list(map.values())

        for i in range(0,len(values)-1):
            if values[i] in values[i+1:]:
                return False

        return True
