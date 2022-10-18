class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        stack = []
        
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    top = stack.pop()    
                    dp[i+1] = dp[top] + (i - top + 1)
        
        return max(dp)
        