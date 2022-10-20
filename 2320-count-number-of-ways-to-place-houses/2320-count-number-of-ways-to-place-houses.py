class Solution:
    def countHousePlacements(self, n: int) -> int:
        check = {1: 2, 2: 3} 
        def dp(i):
            if i in check:
                return check[i]
            
            check[i] = dp(i-1) + dp(i-2)
            return check[i]
    
        return (dp(n)**2) % (10**9+7)
    