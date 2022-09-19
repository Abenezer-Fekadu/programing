class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        bound = lambda row, col: 0 <= row < len(mat)+1 and 0 <= col < len(mat[0])+1  
        dp =  [[0] * (col + 1) for _ in range(row+1)]
        
        for i in range(1, row+1):
            for j in range(1, col+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
                

        for i in range(row):
            for j in range(col):
                col1, col2 = max(0, j-k), min(j+k, col-1)
                row1, row2 = max(0, i-k), min(i+k, row-1)
                
                topRight = dp[row1][col2+1] if row1 > 0 else 0
                topLeft = dp[row1][col1] if (col1 > 0 and row1 > 0) else 0
                
                bottomLeft = dp[row2+1][col1] if col1 > 0 else 0
                bottomRight = dp[row2+1][col2+1]
                
                mat[i][j] =  bottomRight + topLeft - bottomLeft - topRight 

        return mat
