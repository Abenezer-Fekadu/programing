class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, word = len(s), set(wordDict)
    
        dp = [True] + [False] * n

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word:
                    dp[i] = True

        return dp[n]