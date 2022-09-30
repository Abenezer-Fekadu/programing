class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        check = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, "empty") for _, R, _ in buildings])   
        
        ans, max_heap = [[0, 0]], [(0, float('inf'))]
        for x, h, R in check:
            while x >= max_heap[0][1]:
                heappop(max_heap)
                
            if h:
                heappush(max_heap, (h, R))
                
            max_height = -max_heap[0][0]
            
            if ans[-1][1] != max_height:
                ans.append([x, max_height])
                
                
        return ans[1:] 