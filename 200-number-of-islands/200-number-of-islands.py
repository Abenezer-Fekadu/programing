class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, group):
            visited.add((i, j))
            group.add((i, j))
            grid[i][j] = '#'
            for neighbours in Adj:
                new_row, new_col = i + neighbours[0], j + neighbours[1]
                if self.isValid(new_row, new_col, grid) and grid[new_row][new_col] == '1' :
                    dfs(new_row, new_col, group) 
                    
            
    
        if not grid:
            return 0
        
        Adj = [[0,1], [1,0], [-1, 0], [0,-1]]    
        answer = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    group = {(i,j)}
                    dfs(i, j, group)
                    answer.append(group)
        
        return len(answer)
    
    
    def isValid(self, row, col, grid):
        return  (row >= 0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))