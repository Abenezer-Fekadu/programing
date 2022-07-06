class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = {}
        def calculate(n):
        
            if n in stairs:
                return stairs[n]
            
            stairs[n] = n if n <= 2 else calculate(n - 1) + calculate(n - 2)
            return stairs[n]

        return calculate(n)