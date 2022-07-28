class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
            
            
        for w in t:
            char = chars.get(w) 
            if char and char >= 1:
                chars[w] -= 1
            else:
                return False
            
        return True
        