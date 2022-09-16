class Solution:
    def numTrees(self, n: int) -> int:
        check = {}
        
        def helper(n):
            if n in check:
                return check[n]
            if n <= 1:
                return 1
            
            result = 0
            for i in range(n):
                result += helper(i) * helper(n - 1 - i)

            check[n] = result
            return result
    
        return helper(n)