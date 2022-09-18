class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        bound = lambda row, col: 0 <= row < len(matrix) and 0 <= col < len(matrix)
        adj = [[1, -1], [1, 0], [1, 1]]
        check = {}
        
        def recursive(row, col):
            if (row, col) in check:
                return check[(row, col)]
            
            if row == len(matrix) -1:
                return matrix[row][col] 
            
            val = inf
            for i in adj:
                new_row, new_col = row + i[0], col + i[1]
                if bound(new_row, new_col):
                    val = min(matrix[row][col] + recursive(new_row, new_col), val)
            
            check[(row, col)] = val
            return check[(row, col)]
        
        ans = inf
        for i in range(len(matrix)):
            ans = min(recursive(0, i), ans)
        
        return ans
        
                         
            
            