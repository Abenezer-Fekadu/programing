class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        row = 0
        col = 0
        for _ in range(n//2):
            last = n - col - 1
            while col < last:
                matrix[row][col], matrix[col][n-1-row] = matrix[col][n-1-row], matrix[row][col]
                matrix[row][col], matrix[n-1-row][n-1-col] = matrix[n-1-row][n-1-col], matrix[row][col]
                matrix[row][col], matrix[n-1-col][row]  = matrix[n-1-col][row], matrix[row][col]
                
                col += 1
            
            row += 1
            col = row