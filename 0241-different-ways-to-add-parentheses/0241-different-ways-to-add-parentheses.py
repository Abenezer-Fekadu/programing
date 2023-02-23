class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        op = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b}

        memo = {}        
        def dp(s):
            if s.isdigit(): 
                return [int(s)]
            if s not in memo: 
                ans = []
                for i in range(len(s)):
                    if s[i] in "+-*":
                        left, right = dp(s[:i]), dp(s[i+1:])
                        for a in left:
                            for b in right:
                                ans.append(op[s[i]](a, b))
                memo[s] = ans
            return memo[s]
        
        return dp(expression)