class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]
        adj = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        bound = lambda row, col : 0 <= row < m and 0 <= col < n
        for w in walls:
            grid[w[0]][w[1]] = 'w'
            
        for g in guards:
            grid[g[0]][g[1]] = 'g'
            
        for guard in guards:
            for d in adj:
                new_row, new_col = guard[0] + d[0], guard[1] + d[1] 
                while bound(new_row, new_col) and grid[new_row][new_col] != 'w' and grid[new_row][new_col] != 'g':
                    
                    grid[new_row][new_col] = 'gg'
                    new_row += d[0] 
                    new_col += d[1]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    
        return count
            