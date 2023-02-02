class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            word = log.split()
            if word[1].islower():
                letters.append(word)
            else:
                digits.append(log)
        
        letters.sort(key=lambda x: (x[1:], x[0]))
        ans = []
        for word in letters:
            ans.append(" ".join(word))
        return ans + digits
                
        
        
        