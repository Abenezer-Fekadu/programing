class Solution:
    def convert(self, s: str, numRows: int) -> str:		
        ans, move, reverse, size = ['']*numRows,  0,  False, numRows -1
        if numRows == 1:
            return s
        
        for index, c in enumerate(s):
            if size == index:
                size = index + numRows + (numRows - 2)
                reverse = True
            elif move == 0 and index !=0:
                reverse = False
                
            if not reverse:
                ans[move] += c
                move += 1
            else:
                ans [move] += c
                move -= 1

        return(''.join(ans))
