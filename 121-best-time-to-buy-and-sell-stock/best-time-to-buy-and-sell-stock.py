class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        mini = prices[0]
        for i in prices:
            if mini < i:
                sub = i - mini
                profit = max(sub,profit)
                
            else:    
                mini = i
        return profit     



       