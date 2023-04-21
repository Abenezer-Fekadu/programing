class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j, visited):
            visited.add((i,j))
            temp.add((i,j))

            for neighbours in Adj:
                new_row, new_col = i + neighbours[0], j + neighbours[1]
                if self.isValid(new_row, new_col, board):
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        dfs(board, new_row, new_col, visited)
                    continue
                      
        surrounded = set()
        temp = set()
        visited = set()
        Adj = [[0,1], [1,0], [-1, 0], [0,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and  (i == len(board)-1 or j == len(board[0])-1 or i == 0 or j == 0):
                    dfs(board, i, j, visited)
                      
                        
        for i in range(len(board)):
            for j in range(len(board[0])): 
                if board[i][j] == 'O' and  (i,j) not in temp:
                    board[i][j] = "X"
                        
    def isValid(self, row, col, board):  
        return (row >= 0) and (row < len(board)) and (col >= 0) and (col < len(board[0])) and board[row][col] == "O"
    