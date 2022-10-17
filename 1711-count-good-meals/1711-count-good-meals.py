class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = defaultdict(int)
        mod = 10**9 + 7
        
        count = 0
        for num in deliciousness: 
            for p in range(22): 
                count += freq[2**p - num]
                
            freq[num] += 1
        return count % mod