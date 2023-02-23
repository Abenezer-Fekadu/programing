class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        first = (rec1[1] >= rec2[3]) or (rec2[1] >= rec1[3])
        second = (rec1[2] <= rec2[0]) or (rec2[2] <= rec1[0])
        return not (first or second)