class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        adj = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ans = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            
            if grid[i][j] == 1:
                return True
            
            grid[i][j] = 1 
        
            l, r = dfs(i, j-1), dfs(i, j+1)
            t, b = dfs(i-1, j), dfs(i+1, j)
            return l and r and t and b
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0 and dfs(i, j):
                    ans += 1
        
        return ans