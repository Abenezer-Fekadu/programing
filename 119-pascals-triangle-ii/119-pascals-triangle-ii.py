class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        def recursive(index):
            if index == rowIndex: return res
            
            temp = [1]
            for i in range(len(res[-1]) - 1):
                val = res[-1][i] + res[-1][i+1]
                temp.append(val)
                
            res.append(temp + [1])
            return recursive(index+1)
        
        
        return recursive(0)[rowIndex]
        
        