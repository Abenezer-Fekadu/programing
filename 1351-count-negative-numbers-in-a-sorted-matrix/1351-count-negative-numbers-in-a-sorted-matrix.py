class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        
        row, col = len(grid)-1, 0
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                ans += (len(grid[0]) - col)
                row -= 1
            else:
                col += 1
            
        return ans
 

