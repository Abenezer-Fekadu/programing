class DetectSquares:
    def __init__(self):
        self.points = defaultdict(self.val)
    def val(self):
        return defaultdict(int)
    
    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        
        ans = 0
        for y1, count in self.points[x].items():
            if y1 != y:
                diff = y - y1
                for x1 in (x + diff, x - diff):
                    ans += count * self.points[x1][y] * self.points[x1][y1]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)