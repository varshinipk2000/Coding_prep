Can place flowers (https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if(flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i+1==len(flowerbed) or flowerbed[i+1]==0)):
                flowerbed[i]=1
                n-=1 
                if n==0:
                    return True
        return False   
        
