class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(num, val):
            if val == 0:
                if num == endPos:
                    return 1
                return 0  
            
            f = dfs(num + 1, val-1)
            l = dfs(num - 1, val-1)
            
            return l + f
        
        
        return dfs(startPos, k) % mod
        
        