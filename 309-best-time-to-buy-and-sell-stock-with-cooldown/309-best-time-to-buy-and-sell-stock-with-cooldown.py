class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[0, 0] for _ in range(n + 1)]
        dp[n][0] = dp[n][1] = 0
        
        for i in range(n-1, -1, -1):
            for canBuy in range(2):
                result = float('-inf')
                if canBuy:
                    result = max(-prices[i] + dp[i+1][0],
                                dp[i+1][1])
                else:
                    result = max(prices[i] + (dp[i+2][1] if i+2 < n else 0),
                                dp[i+1][0])
                
                dp[i][canBuy] = result
        
        return dp[0][1]