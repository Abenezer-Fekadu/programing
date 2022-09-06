class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibonacci(num):
            if num in memo:
                return memo[num]
            
            memo[num] = num if num < 2 else fibonacci(num-2) + fibonacci(num-1)
            return memo[num]
    
        return fibonacci(n)