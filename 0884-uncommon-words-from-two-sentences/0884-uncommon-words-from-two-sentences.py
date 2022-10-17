class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = Counter(s1.split())
        words2 =  Counter(s2.split())
        
        ans = []
        for word in words1:
            if words1[word] == 1 and word not in words2:
                    ans.append(word)
                    
        for word in words2:
            if words2[word] == 1 and word not in words1:
                ans.append(word)
                
        return ans
    
    
