class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(p)        
        p = sorted(p)
        
        ans = []
        for i in range(len(s)-size+1):
            val = sorted(s[i:i+size])
            if val == p:
                ans.append(i)
        return ans
