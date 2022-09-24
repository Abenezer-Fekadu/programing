class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lst = sorted(count.keys(), key=lambda x: -count[x])
        
        return [lst[i] for i in range(k)]
    
    