class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(n, left):
            if n == 1 : 
                return 1
            if left:
                return 2*helper(n//2, False)
            elif n%2 == 1:
                return 2*helper(n//2, True)
            else:
                return 2*helper(n//2, True) - 1
            
        return helper(n, True)