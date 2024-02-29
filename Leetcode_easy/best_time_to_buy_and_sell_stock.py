# Best time to buy and sell stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)==1:
            return 0

        maxele = -1
        maxsum = -1

        for i in range(len(prices)-1,0,-1):
            maxele = max(maxele,prices[i])
            maxsum = max(maxsum, maxele - prices[i-1])

        if maxsum<0:
            return 0
        return maxsum        
