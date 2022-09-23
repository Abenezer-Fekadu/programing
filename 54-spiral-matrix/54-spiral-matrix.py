class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        adj = [0, 1]
        bound = lambda row, col: col < 0 or col >= n or row  < 0 or row >= m

        ans = []
        def solve(row, col, count):
            ans.append(matrix[row][col])
            matrix[row][col] = 1000 
            
            if count == m *n - 1 :
                return 
            
            if bound(row + adj[0], col + adj[1]) or matrix[row + adj[0]][col + adj[1]] == 1000:
                adj[0], adj[1] = adj[1], -1*adj[0]
            
            new_row, new_col = row + adj[0], col + adj[1]
            solve(new_row, new_col, count+1)

            return 
        
        solve(0, 0, 0)
        return ans
        
        