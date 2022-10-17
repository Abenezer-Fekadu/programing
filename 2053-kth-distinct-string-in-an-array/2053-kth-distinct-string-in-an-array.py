class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        for c in count:
            if count[c] == 1:
                k -= 1
            if k == 0:
                return c
        return ""
                
        