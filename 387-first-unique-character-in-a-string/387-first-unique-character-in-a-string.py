class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        else:
            return -1