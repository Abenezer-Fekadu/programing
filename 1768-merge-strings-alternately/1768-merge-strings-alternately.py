class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s, first = "", True
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            if first:
                s += word1[i]
                i += 1
                first = False
            else:
                s += word2[j]
                j += 1
                first  = True
                
        m = word1[i:] or word2[j:]
        
        return s + m