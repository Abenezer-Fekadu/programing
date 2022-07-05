class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            val = i
            summ = 0
            while val:
                summ += val % 10
                val //= 10 
                
            if summ % 2 == 0:
                count += 1
                
        return count