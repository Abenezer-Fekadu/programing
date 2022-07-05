class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = num // 3
        rem = num % 3
        
        return [mid-1, mid, mid+1] if rem == 0 else []