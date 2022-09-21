class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = defaultdict(list)
        
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': 
                    if char in check:
                        for pos in check[char]:
                            if (pos[0] == x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    check[char].append((x,y))
   
        return True