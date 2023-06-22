class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]
            
            val = 0
            if buy:
                val = max(dfs(i+1, not buy) - prices[i], dfs(i+1, buy))
            else:
                val = max(dfs(i+1, not buy) + prices[i] - fee, dfs(i+1, buy))
            
            memo[(i,buy)] = val
            return memo[(i, buy)]
        
        return dfs(0, True)