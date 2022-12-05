class Solution:
    def isBound(self, m, n, row, col):
        return  0 <= row < m and 0 <= col < n
    
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        sr, sc = start[0], start[1]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        seen = set()
        result = []
        
        q = [(0, grid[sr][sc], sr, sc)]
        while q:
            dis, price, row, col = heappop(q)
            if (row, col) not in seen:
        
                seen.add((row, col))
                if price != 1 and pricing[0] <= price <= pricing[1]:
                    result.append([row, col])
                    
                if len(result) == k:
                    return result
                
                for dr, dc in directions:
                    next_row, next_col = row + dr, col + dc
                    if self.isBound(m, n, next_row, next_col) and (next_row, next_col) not in seen:
                        temp = grid[next_row][next_col]
                        if temp != 0:
                            heappush(q, (dis + 1, temp, next_row, next_col))

        return result