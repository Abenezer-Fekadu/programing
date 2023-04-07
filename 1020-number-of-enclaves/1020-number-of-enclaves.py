class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, visited):
            visited.remove((i,j))
            for neighbours in Adj:
                new_row, new_col = i + neighbours[0], j + neighbours[1]
                if self.isValid(new_row, new_col, grid, visited):
                    dfs(grid, new_row, new_col, visited)
                    continue
                              
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1:
                    visited.add((i, j))
               

        Adj = [[0,1], [1,0], [-1, 0], [0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and  (i == len(grid)-1 or j == len(grid[0])-1 or i == 0 or j == 0) and (i, j) in visited:
                    dfs(grid, i, j, visited)
             
        return len(visited)
    
    
    
    def isValid(self, row, col, grid, visited):  
        return (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0])) and grid[row][col] == 1 and (row, col) in visited
    