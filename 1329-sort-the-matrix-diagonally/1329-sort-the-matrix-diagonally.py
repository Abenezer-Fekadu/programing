class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        diag = defaultdict(list)
        for i in range(m):
            for j in range(n):
                diag[i - j].append(mat[i][j])

        for k in diag:
            diag[k].sort(reverse=True)
            
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[i - j].pop()
                
        return mat
    