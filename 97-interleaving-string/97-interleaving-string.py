class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        
        curr, nxt = set([(-1, -1)]), set()
        count = 0
        
        while curr and count < len(s3):
            for i, j in curr:
                if i + 1 < n and s1[i + 1] == s3[count]:
                    nxt.add((i + 1, j))
                if j + 1 < m and s2[j + 1] == s3[count]:
                    nxt.add((i, j + 1))
                    
            curr, nxt = nxt, set()
            if curr:
                count += 1
    
        return count == len(s3)