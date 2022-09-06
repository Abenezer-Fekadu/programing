class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def solve(num):
            if num < 0:
                return 0
            if num in memo:
                return memo[num]
            
            memo[num] = num if num < 2 else solve(num-1) + solve(num-2) + solve(num-3)
            return memo[num]
        
        return solve(n)