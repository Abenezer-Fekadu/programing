class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        if grid[0][0] == 1 or grid[m-1][n-1] == 1: return -1
        
        ans = 1
        queue = deque([(0, 0)])
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == m-1 and c == n-1: 
                    return ans
                
                for dr, dc in adj:
                    new_row, new_col = r + dr, c + dc
                    if new_row < 0 or new_row == m or new_col < 0 or new_col == n or grid[new_row][new_col] == 1: continue
                        
                    grid[new_row][new_col] = 1  
                    queue.append((new_row, new_col))
            ans += 1
        return -1
    