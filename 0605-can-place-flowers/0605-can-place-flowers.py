class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev, consumed = 0, False
        for i in flowerbed:
            if n < 0:
                return True
            if not i and not prev:
                n -= 1
                prev = 1
                consumed = True
            elif i and consumed:
                n += 1
                prev = i
                consumed = False
            else:
                prev = i
                consumed = False

        return n <= 0