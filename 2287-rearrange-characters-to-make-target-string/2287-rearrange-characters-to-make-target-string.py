class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count1 = Counter(s)
        count2 = Counter(target)
        
        minn = inf
        for j in count2.keys():
            minn = min(minn, count1[j] // count2[j])
            
        return minn 
        
    
        
        