class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            if count[c] < 1:
                count[c] += 1
            else:
                return c
        