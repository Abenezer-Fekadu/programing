class Solution:
    def isBound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        visited = 0
        sr, sc = 0, 0       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1 or grid[i][j] == 1:
                    visited ^= (1 << ((i*n) + j))
                if grid[i][j] == 1:
                    sr = i
                    sc = j
        count = 0 
        def backtrack(row, col):
            nonlocal count, visited
            if grid[row][col] == 2:
                if visited.bit_count() == m*n:
                    count += 1
                return
                        
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if  self.isBound(next_row, next_col, m, n):
                    bit = 1 if visited & (1 << ((next_row*n) + next_col)) else 0
                    if not bit and grid[next_row][next_col] != -1:
                        visited ^= (1 << ((next_row*n) + next_col)) 
                        backtrack(next_row, next_col)
                        visited ^= (1 << ((next_row*n) + next_col))
            return
        
        backtrack(sr, sc)
        return count
        
                  
                  
                  
            