class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        
        ans  = []
        for word in words:
            for i in range(len(words)):
                if words[i] != word:
                    w = words[i].split(word)
                    if w[0] != words[i]:
                        ans.append(word)
                        break
        return ans