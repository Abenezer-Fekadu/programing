class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        count = 1
        ans = [1]
    
        while count < n:
            val = min(ans[i2]*2, ans[i3]*3, ans[i5]*5)
            ans.append(val)

            if val == ans[i2]*2:
                i2 += 1
            if val == ans[i3]*3:
                i3 += 1
            if val == ans[i5]*5:
                i5 += 1

            
            count += 1
        
        return ans[-1]
        
        
