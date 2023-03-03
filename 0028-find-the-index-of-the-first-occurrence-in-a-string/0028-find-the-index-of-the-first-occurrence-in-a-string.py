class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        
        lst = []
        if needle not in haystack:
            return -1
        else:
            lst = haystack.split(needle)
            
        return len(lst[0])
        
        