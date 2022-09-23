class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(1, n+1):
            size = i.bit_length()
            
            ans = (ans << size) | i
            ans %= mod
        
        return ans 
                 
    
        
                    