class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        s = []
        for c in lst:
            s.append(c[::-1])    
        
        return " ".join(s)