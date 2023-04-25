class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        strs.sort()
        size = len(strs)
        
        minn = min(len(strs[0]), len(strs[size-1]))
        i = 0
        while i < minn and strs[0][i] == strs[size-1][i]:
            i += 1 
        return strs[0][:i]