class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        w = defaultdict(int)        
        ans = []
        for word in words2:                 
            c2 = Counter(word)
            for ch in c2:
                w[ch] = max(w[ch], c2[ch])

                
        for word in words1:                    
            c1 = Counter(word)
            for ch in w:
                if c1[ch] < w[ch]: 
                    break
            else:
                ans.append(word)              
        return ans 