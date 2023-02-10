class Solution:
    def isBound(self, n, row, col):
        return 0 <= row < n and 0 <= col < n

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    
        if len(queue) == n*n or len(queue) == 0:
            return -1

        ans = 0
        while queue:
            row, col = queue.popleft()
            ans = max(ans, grid[row][col])
            for dr, dc in directions:
                next_row, next_col =  row + dr, col + dc
                if self.isBound(n, next_row, next_col) and grid[next_row][next_col] == 0:
                    grid[next_row][next_col] = 1 + grid[row][col]
                    queue.append((next_row, next_col))
        
        return ans - 1 

                
