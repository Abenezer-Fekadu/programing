class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        for c in s:
            if c == "b":
                count += 1
                        
        ans = count
        size = count
        for c in s:
            if c == "b":
                size -= 1
            else:
                size += 1
            ans = max(ans, size)
        
        return len(s) - ans