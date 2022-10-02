class Solution:
    def deleteString(self, s: str) -> int:    
        n = len(s)
        
        @cache
        def dfs(i):
            if i == n:
                return 0
            
            ans = 1
            j = 1
            while i+2*j <= n and n-i-j+1 > ans:
                if s[i:i+j] == s[i+j:i+2*j]:
                    ans = max(ans, 1 + dfs(i+j))
                    
                j += 1
            return ans
        
        return dfs(0)
        
        
        