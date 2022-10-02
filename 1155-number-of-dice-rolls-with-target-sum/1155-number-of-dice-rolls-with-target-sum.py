class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1
            
            if (n, target) in memo:
                return memo[(n, target)]
            
            ans = 0
            for m in range(max(0, target-k), target):
                ans += dp(n-1, m)
                
            memo[(n, target)] = ans
            return memo[(n, target)]
        
        return dp(n, target) % (10**9 + 7)