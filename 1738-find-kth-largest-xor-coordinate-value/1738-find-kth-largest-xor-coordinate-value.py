class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pref = [[0]*(n+1) for _ in range(m+1)]
        
        nums = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                pref[i][j] = pref[i-1][j] ^ pref[i][j-1] ^ matrix[i-1][j-1] ^ pref[i-1][j-1]
                heappush(nums, pref[i][j])
                if len(nums) > k:
                    heappop(nums)
                    
        return heappop(nums)
        