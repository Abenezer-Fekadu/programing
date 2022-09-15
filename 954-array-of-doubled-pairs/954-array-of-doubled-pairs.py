class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        
        arr.sort()
        
        for num in arr:
            count[num] += 1
            
        for num in arr:
            if count[num] > 0 and count[2*num] > 0:
                count[num] -= 1
                count[2*num] -= 1        
        
        for v in count.values():
            if v != 0:
                return False
            
        return True