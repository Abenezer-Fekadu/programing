class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(b) > len(a):
            return self.findLUSlength(b, a)
        
        return -1 if a == b else len(a)

            