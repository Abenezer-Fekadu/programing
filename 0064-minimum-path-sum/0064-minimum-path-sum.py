class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        dp = [[0]*len(grid[0]) for i in grid]
        
        def solve(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            elif not bound(i, j):
                return inf
            
            if dp[i][j] != 0:
                return dp[i][j]
            result = grid[i][j] + min(solve(i+1, j), solve(i, j+1))
            
            dp[i][j] = result
            return dp[i][j]
        
 
        return solve(0, 0)
    
        
            
            