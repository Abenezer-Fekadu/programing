class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        ans = 0
        for j in range(m):
            for i in range(1, n):
                if strs[i-1][j] > strs[i][j]:
                    ans += 1
                    break
        return ans
                
        