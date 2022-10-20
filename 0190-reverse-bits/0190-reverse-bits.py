class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            val = 1 if n & (1 << i) else  0 
            
            ans <<= 1
            ans = (ans | val)
            
        return ans