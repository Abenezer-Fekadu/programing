class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            m = {}
            n = {}
            if len(word) == len(pattern):
                check = True
                for i in range(len(word)):
                    w1 = m.get(pattern[i])
                    w2 = n.get(word[i])
                    if (w1 or w2) and (w1 != word[i] or w2 != pattern[i]):
                        check = False
                    elif not w1 or not w2 :
                        m[pattern[i]] = word[i]
                        n[word[i]] = pattern[i]
                        
                if check:
                    ans.append(word)
        
        return ans
                    
                    
                    
                