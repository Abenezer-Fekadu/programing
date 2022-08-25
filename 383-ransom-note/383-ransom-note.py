class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        
        for c in ransomNote:
            if count[c] > 0:
                count[c] -= 1  
            else:  
                return False
        
        return True