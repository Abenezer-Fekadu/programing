class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)

        check = False 
        for  i, c in enumerate(num): 
            d = int(c)
            if d < change[d]: 
                check = True
                num[i] = str(change[d])
                
            elif d > change[d] and check: 
                break
                
        return "".join(num)