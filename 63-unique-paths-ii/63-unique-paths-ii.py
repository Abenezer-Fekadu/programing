class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        bound = lambda row, col : 0 <= row < m and 0 <= col < n
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = '#'
        
        def solve(i, j):
            if not bound(i, j) or obstacleGrid[i][j] == '#':
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            if obstacleGrid[i][j] not in ['#', 0]:
                return obstacleGrid[i][j]
            
            obstacleGrid[i][j] = solve(i+1, j) + solve(i, j+1)
            return obstacleGrid[i][j]
        
        val = solve(0,0)
        return val