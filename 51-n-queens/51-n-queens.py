class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, dif, summ):
            
            size = len(queens)
            if size == n:
                result.append(queens)
                return
            
            for q in range(n):
                if q not in queens and size-q not in dif and size+q not in summ:
                    dfs(queens+[q], dif+[size-q], summ+[size+q])
                    
        result = []
        dfs([],[],[])
        
        return [["."*i + "Q"+"."*(n-i-1) for i in ans] for ans in result]