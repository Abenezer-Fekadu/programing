class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = defaultdict(int)
        ans = 0
        maxfreq = 0 
        while r < len(s):
            count[s[r]] += 1
            
            maxfreq = max(maxfreq, count[s[r]])
            if (r-l+1 - maxfreq) > k:
            
                count[s[l]] -= 1
                l += 1
                
            ans = max(ans, r-l+1)
            r += 1
        return ans
            
        
        