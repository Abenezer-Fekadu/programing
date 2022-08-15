class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        
        nums = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == 'I' and s[i+1] in ('V', 'X'):
                nums += romans[s[i+1]] - romans[s[i]]
                i += 2
            elif i + 1 < len(s) and s[i] == 'X' and s[i+1] in ('L', 'C'):
                nums += romans[s[i+1]] - romans[s[i]]
                i += 2
            elif i + 1 < len(s) and s[i] == 'C' and s[i+1] in ('D', 'M'):
                nums += romans[s[i+1]] - romans[s[i]]
                i += 2
            else:
                nums += romans[s[i]]
                i += 1
                
        return nums