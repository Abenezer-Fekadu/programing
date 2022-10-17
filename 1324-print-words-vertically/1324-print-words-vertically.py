class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        size = max(len(word) for word in words)
        
        ans = ["" for i in range(size)]
        for word in words:
            for i in range(size):
                if i < len(word):
                    ans[i] += word[i]
                else:
                    ans[i] += " "
            
        return [word.rstrip() for word in ans]