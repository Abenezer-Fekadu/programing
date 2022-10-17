class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def twoMins(arr):
            first = second  = inf
            for num in arr:
                if num < first:
                    second = first
                    first = num
                elif num < second:
                    second = num
            return (first, second)

        
        for i in range(1, n):
            min1, min2 = twoMins(grid[i-1])
			
            for j in range(n):
                minVal = min1
                if min1 == grid[i-1][j]:     
                    minVal = min2            
					
                grid[i][j] = grid[i][j] + minVal
        
        return min(grid[-1])