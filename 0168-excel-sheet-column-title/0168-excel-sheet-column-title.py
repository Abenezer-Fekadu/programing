class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = []
        for i in range(65, 91):
            letters.append(chr(i))
            
        ans = []
        while columnNumber > 0:
            val = columnNumber - 1
            
            ans.append(letters[val%26])
            columnNumber = val // 26
         
        ans.reverse()
        return ''.join(ans)