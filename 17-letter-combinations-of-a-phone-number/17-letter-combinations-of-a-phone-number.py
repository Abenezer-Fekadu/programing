class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        ans = []
        if len(digits) == 0:
            return ans
        
        def check(s, index, digits):
            if len(s) == len(digits):
                ans.append(s)
                return
            
            for i in digits[index]:
                for j in letters[i]:
                    check(s+j, index+1, digits)   
                    
                    
        check("", 0, digits)
        
        return ans
