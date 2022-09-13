class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        unicode = []
        for i in range(len(data)):
            x = bin(data[i]).replace("0b", "")
            if len(x) < 8:
                x = '0' * (8 - len(x)) + x
            unicode.append(x)
            
        curr = None
        count = 0
        for i in range(len(unicode)):
            if count > 0:
                if unicode[i][:2]!='10':
                    return False
                count -= 1
                
            elif count == 0 and unicode[i][:2] == '10':
                return False
            else:
                for j in range(5):
                    if unicode[i][j] == '0':
                        if j == 0:
                            curr = 1
                        else:
                            curr = j
                            count = j - 1
                        break
                else:
                    return False
        
        
        if count > 0:
            return False
        return True