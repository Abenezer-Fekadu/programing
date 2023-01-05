class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
            points.sort()
            ans, first = 1, points[0]
            for start, end in points:
                if start > first[1]:
                    ans += 1
                    first = [start, end]
                else:
                    first = [start, min(end, first[1])]

            return ans
    