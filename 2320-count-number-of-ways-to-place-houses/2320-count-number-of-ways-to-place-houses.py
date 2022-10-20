class Solution:
    def countHousePlacements(self, n: int) -> int:
        x, y = 1, 2
        for i in range(1, n):
            x, y = y, x + y
        return (y ** 2) % (10**9 + 7)