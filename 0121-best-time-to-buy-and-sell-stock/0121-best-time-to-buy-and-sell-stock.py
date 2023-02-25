class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < price:
                price = prices[i]

            profit = max(prices[i] - price, profit)
            
        return profit   