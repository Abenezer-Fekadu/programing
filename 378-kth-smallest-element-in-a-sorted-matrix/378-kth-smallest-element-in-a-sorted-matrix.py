class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        lst = [(val[0], i, 0) for i, val in enumerate(matrix)]
        
        heapify(lst)
        num = float("-inf")
        
        for i in range(k-1):
            val = heappop(lst)

            num = val[0]
                        
            if val[2] + 1 < len(matrix):
                heappush(lst, (matrix[val[1]][val[2]+1], val[1], val[2]+1))
             
        return lst[0][0]