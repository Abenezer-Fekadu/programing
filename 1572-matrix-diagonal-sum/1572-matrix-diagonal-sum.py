class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        seen = set()
        
        pr, pc = 0, 0
        sr, sc = 0, n-1
        
        def search(i, j, d):
            ans = 0  
            while 0 <= i < m and 0 <= j < n:
                if (i, j) not in seen:
                    ans += mat[i][j]
                    seen.add((i, j))
                if d == -1:
                    j -= 1
                else:
                    j += 1
                    
                i += 1
                
            return ans
        
        
        return search(pr, pc, 1) + search(sr, sc, -1)