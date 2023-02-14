class Solution:
    def sumZero(self, n: int) -> List[int]:
         return [-n*(n-1)//2] + list(range(1,n))