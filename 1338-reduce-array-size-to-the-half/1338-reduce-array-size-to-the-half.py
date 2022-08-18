class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
                
        value_count, ans = 0, 0
        items = sorted(count.items(), key=lambda x:-x[1])       
        for key, val in items:
            value_count += val
            ans += 1
            
            if value_count >= len(arr) // 2:
                return ans
            
        
        
        