class Solution:
    def reverseStr(self, s: str, k: int) -> str:
 
        ans = []
        l = 0
        while l < len(s):
            r = l + 2*k
            if l+k-1 < len(s):
                for i in range(l+k-1, l-1, -1):
                    ans.append(s[i])
                    
                ans.append(s[l+k: l+2*k])
            else:
                for i in range(len(s)-1, l-1, -1):
                    ans.append(s[i])
                    
            l = r
                
        return "".join(ans)
            
            
            
            
        