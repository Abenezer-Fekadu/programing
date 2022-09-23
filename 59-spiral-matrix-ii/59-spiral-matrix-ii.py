class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        bound = lambda row, col: 0 <= row < n and 0 <= col < n 
        adj = [0, 1]
        
        ans = [[0] * n for i in range(n)]
        def solve(row, col, i):
            if i == n**2 + 1:
                return        
            ans[row][col] = i
    
            if not bound(row + adj[0], col + adj[1]) or ans[row + adj[0]][col + adj[1]] != 0:
                adj[0], adj[1] = adj[1], -1*adj[0]
              
            new_row, new_col = row + adj[0], col + adj[1]
            
            solve(new_row, new_col, i+1) 
            
        solve(0, 0, 1)
        return ans