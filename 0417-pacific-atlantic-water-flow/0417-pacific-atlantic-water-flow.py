class Solution:
    def isBound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        derections = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        pacific_coords = set()        
        atlantic_coords = set()
        
        def dfs(row, col, prev_height, visited):
            if not self.isBound(row, col, m, n) or (row, col) in visited:
                return            

            height = heights[row][col]
            if height < prev_height:
                return 
            
            visited.add((row, col))
            for dr, dc in derections:    
                next_row, next_col = row + dr, col + dc
                dfs(next_row, next_col, height, visited)
                
        # check for cells that are connected to the pacific oceans
        for col in range(n):
            dfs(0, col, 0, pacific_coords)
        for row in range(m):
            dfs(row, 0, 0, pacific_coords)
            
            
        # check for cells that are connected to the pacific oceans
        for row in range(m):
            dfs(row, n - 1, 0, atlantic_coords) 
        for col in range(n):
            dfs(m - 1, col, 0, atlantic_coords)
            
            
        return list(pacific_coords & atlantic_coords)