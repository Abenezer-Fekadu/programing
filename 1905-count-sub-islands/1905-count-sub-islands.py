class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        bound = lambda row, col: 0 <= row < len(grid1) and 0 <= col < len(grid1[0])
        adj = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        
        def solve(row, col):
            grid2[row][col] = 0
            queue = deque([[row, col]])
            
            res = True 
            while queue:
                top = queue.popleft()
                if grid1[top[0]][top[1]] != 1:
                    res = False
                for a in adj:
                    new_row, new_col = top[0] + a[0], top[1] + a[1]
                    if bound(new_row, new_col) and grid2[new_row][new_col]:
                        queue.append([new_row, new_col])
                        grid2[new_row][new_col] = 0
                
            return res
                        
          
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j]:
                    check = solve(i, j)
                    count = count + 1 if check else count + 0
                       
        return count                     
                    
        