class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right =  0, len(nums) - 1
        best = 0
        while left <= right:
            mid = left + (right -left) // 2
            
            
            if nums[mid] >= target:
                right = mid-1
                
            else:
                best = mid + 1
                left = mid + 1
                
        return best
                