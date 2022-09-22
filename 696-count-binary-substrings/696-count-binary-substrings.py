class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        ans = 0
        currchar = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] != currchar:
                currchar = s[i] 
                ans += min(count, prev)
                prev = count
                count = 1
            else:
                count += 1
                
        ans += min(count, prev)
        return ans