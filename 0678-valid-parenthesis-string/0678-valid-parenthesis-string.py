class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)        
        def dp(i, openCount):
            if i == len(s):
                if openCount == 0:
                    return True
                else:
                    return False
            
            if openCount < 0:
                return False
            
            if s[i] == ')':
                return dp(i+1, openCount - 1)
            elif s[i] == '(':
                return dp(i+1, openCount + 1)
            
            
            return dp(i+1, openCount + 1) or dp(i+1, openCount - 1) or dp(i+1, openCount)
            
        return dp(0, 0)