class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set()
        adj = [[0,1],[1,0],[-1,0],[0,-1]]
        
        ans = 0
        def dfs(row, col):
            if (row, col) in visited:
                return
            
            nonlocal ans
            visited.add((row, col))
            for a in adj:
                new_row, new_col = row + a[0], col + a[1]
                if bound(new_row, new_col) and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col)
                else:
                    ans += 1
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    dfs(i, j)
                    
        return ans
            
            