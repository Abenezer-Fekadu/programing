class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, triangle_dp = len(triangle), {}        
        n = [len(triangle[i]) for i in range(m)]
        
        def calculate(row, col):
            if row >= m or col >= n[row]: 
                return 0
            elif (row,col) in triangle_dp:
                return triangle_dp[(row,col)]
            else:
                triangle_dp[(row,col)] = triangle[row][col] + min(calculate(row+1, col), calculate(row+1, col+1)) 
            
        
            return triangle_dp[(row,col)]

        return calculate(0,0)