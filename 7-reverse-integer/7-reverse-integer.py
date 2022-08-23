class Solution:
    def reverse(self, x: int) -> int:
        mul = 1
        if x < 0:
            x *= -1
            mul = -1
            
        rev = 0
        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x//10
            
        if rev < -2**31 or rev > 2**31-1:
            return 0
        
        return rev * mul