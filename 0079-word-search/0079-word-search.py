class Solution:
    
    def isBound(self, row, col, m, n):
        return 0 <= row < m and 0 <= col < n
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1


        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False

        
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            
#         check using recursive call
        def solve(row, col, i):
            if (row, col) in visited:
                return False
            if i == len(word):
                return True
            
            visited.add((row, col))
            ans = False
            for dr, dc in directions:
                next_row, next_col = dr + row, col + dc
                if self.isBound(next_row, next_col, m, n) and board[next_row][next_col] == word[i]:
                    ans |= solve(next_row, next_col, i + 1)
                    
            visited.remove((row, col))
            return ans
        
#         iterate through the matrix and call search on the first letters 
        start_letter = []    
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    start_letter.append([i, j])
        
        
        for c in start_letter:
            row, col = c
            visited = set()
            if solve(row, col, 1):
                return True
        else:
            return False
        
        