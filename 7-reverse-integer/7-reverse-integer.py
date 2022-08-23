class Solution:
    def reverse(self, x: int) -> int:
        check = True
        if x < 0:
            check = False
            
        x = str(abs(x))
        s = []
        zero = True
        for i in range(len(x)-1, -1, -1):
            if x[i] != 0:
                zero  = False
            if not zero:
                s.append(x[i])
        
        num = "".join(s)
        
        if check and int(num) <= 2**31-1:
            return int(num)
        elif not check and -1*int(num) >= -2**31:
            return -1*int(num)
        else:
            return 0
            