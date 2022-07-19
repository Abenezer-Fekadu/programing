class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        def recursive(index):
            if index == numRows: return ans
            lst = [1]
            for i in range(len(ans[-1]) -1):
                val = ans[-1][i] + ans[-1][i+1]
                lst.append(val)
                           
            ans.append(lst + [1])
            return recursive(index+1)
                           
                          
        return recursive(1)