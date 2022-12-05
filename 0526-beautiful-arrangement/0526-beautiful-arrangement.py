class Solution:
    def countArrangement(self, n: int) -> int:
        def dp(i, seen):
            if i > n:
                return 1
            
            ans = 0
            for j in range(1, n+1):
                if (i % j == 0 or j % i == 0) and j not in seen:
                    seen.add(j)
                    ans += dp(i+1, seen)
                    seen.remove(j)
                    
            return ans
        
        return dp(1, set())