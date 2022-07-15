class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):

            if not self.isValid(i, j, grid):
                return 0
            
            grid[i][j] = 0
            count = 1
            for neighbours in Adj:
                new_row, new_col = i + neighbours[0], j + neighbours[1]
                count += dfs(grid, new_row, new_col) 

            return count   
    

        Adj = [[0,1], [1,0], [-1, 0], [0,-1]]
        ones = [] 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones.append(dfs(grid, i, j)) 
                    
        return max(ones) if ones else 0

    def isValid(self, row, col, grid):
        return  (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0])) and grid[row][col] == 1
    
