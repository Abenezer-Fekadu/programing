class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        adj = [[1, 0],[0, 1],[-1, 0],[0,-1]]
        bound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
  
        seen =  set()
        def dfs(i, j):
            if (i, j) in seen: return True

            seen.add((i, j))            
            count = 0
            for a in adj:
                new_row, new_col = i + a[0], j + a[1]
                if (bound(new_row, new_col) and grid[new_row][new_col] == grid[row][col]):
                    count += dfs(new_row, new_col)
                    
                elif  (new_row, new_col) in seen:
                    count += 1
            
            if count < 4:
                grid[i][j] = color
                
            return True
        
        dfs(row, col)
        return grid
    