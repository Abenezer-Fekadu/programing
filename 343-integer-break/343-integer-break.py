class Solution:
    def integerBreak(self, n: int) -> int:
        check = [0,0,1,2,4,6,9]
        if n < 7:
            return check[n]
        dp = check + [0] * (n-6)
        
        
        for i in range(7, n+1):
            dp[i] = 3*dp[i-3]
            
        return dp[-1]