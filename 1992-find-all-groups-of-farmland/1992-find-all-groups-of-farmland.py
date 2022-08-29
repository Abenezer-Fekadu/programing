class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        bound = lambda row, col: 0 <= row < len(land) and 0 <= col < len(land[0])
        adj = [[0, 1], [1, 0]]
        
        def solve(row, col):
            queue = deque([[row, col]])
            val = [row, col, row, col]
            land[row][col] = 0
            while queue:
                top = queue.popleft()
                for a in adj:
                    new_row, new_col = top[0] + a[0], top[1] + a[1]
                    if bound(new_row, new_col) and land[new_row][new_col]:
                        land[new_row][new_col] = 0
                        queue.append([new_row, new_col])
                
                val[-2] = max(top[0], val[-2])
                val[-1] =  max(val[-1], top[1])             
            return val
                    
                
        ans = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j]:                    
                    ans.append(solve(i, j))
                                        
        return ans