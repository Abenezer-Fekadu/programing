class Solution:
    def numDecodings(self, s: str) -> int:
        r, l = 0, 1
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            ans = 0
            if s[i] != "0":
                if int(s[i:i + 2]) <= 26:
                    ans = l + r
                else:
                    ans = l
                    
            r, l = l, ans
            
        return ans