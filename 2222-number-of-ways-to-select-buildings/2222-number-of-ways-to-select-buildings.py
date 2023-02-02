class Solution:
    def numberOfWays(self, s: str) -> int:
        pref = [int(s[0])]
        for i in range(1, len(s)):
            pref.append(pref[-1] + int(s[i]))
        
        ans = 0
        for i in range(1, len(s)-1):
            left, right = pref[i-1], pref[len(s)-1]-pref[i]
            if s[i] == '0':
                ans += (left)*(right)
            else:
                ans += (i-left) * abs((len(s)-i)-right-1)
            
        return ans
    
    
    
    