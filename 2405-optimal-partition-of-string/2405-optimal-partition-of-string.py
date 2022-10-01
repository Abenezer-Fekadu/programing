class Solution:
    def partitionString(self, s: str) -> int:
        check = set(s[0])
        r = 1
        
        count = 1
        while r < len(s):
            if s[r] not in check:
                check.add(s[r])
            else:
                check = set(s[r])
                count += 1
                
            r += 1
            
        return count