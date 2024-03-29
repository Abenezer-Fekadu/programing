class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0: return j  
            if j == 0: return i 
            
            if word1[i-1] == word2[j-1]:
                return dp(i-1, j-1)
            
            return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        
        return dp(len(word1), len(word2))