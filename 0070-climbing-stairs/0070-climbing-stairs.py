class Solution:
    def climbStairs(self, n: int) -> int:
        check = {}
        # base case for our function
        def dp(num):
            if num == n:
                return 1
            elif num > n:
                return 0
            # if already went this path
            if num in check:
                return check[num]
            
            # count for recursive call function
            check[num] = dp(num+1) + dp(num+2) 
            return check[num]
    
        return dp(0)
