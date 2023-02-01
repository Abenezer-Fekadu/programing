class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        pref =  [[0] * (c + 1) for _ in range(r+1)]
        
        # pref_sum
        for i in range(1, r+1):
            for j in range(1, c+1):
                pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + mat[i-1][j-1]
                
        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                row = [max(0, i-k), min(i+k, r-1)]
                col = [max(0, j-k), min(j+k, c-1)]
                
                ans[i][j] = pref[row[1]+1][col[1]+1]
                if col[0] > 0 and row[0] > 0:
                    ans[i][j] += pref[row[0]][col[0]]
                if row[0] > 0:
                    ans[i][j] -= pref[row[0]][col[1]+1]
                if col[0] > 0:
                    ans[i][j] -= pref[row[1]+1][col[0]]

            
        return ans
