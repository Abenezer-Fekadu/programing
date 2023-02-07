class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            log = log.split('/')
            if log[0] == "..":
                ans = 0 if ans == 0 else ans - 1
            elif log[0] != '.':
                ans += 1
        return ans