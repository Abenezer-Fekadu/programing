class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        
        left = defaultdict(int)
        right = Counter(s)
        count = 0
        for i in range(len(s)):
            left[s[i]] += 1
            if right[s[i]] <= 1:
                del right[s[i]]
            else:
                right[s[i]] -= 1
            
            if len(left) == len(right):
                count += 1
                
        return count
    
    