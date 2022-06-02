class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0]*len(matrix) for i in matrix[0]]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                ans[col][row] = matrix[row][col]
                
                
        return ans