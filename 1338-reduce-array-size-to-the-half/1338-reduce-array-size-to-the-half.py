class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        lst = []
        
        value_count = 0
        for k, v  in count.items():
            lst.append([-v, k])
            
        heapify(lst)
        
        ans = 0
        for i in lst:
            value_count += -heappop(lst)[0]
            ans += 1
            if value_count >= len(arr)//2:
                return ans
            
        
        
        