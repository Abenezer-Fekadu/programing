class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums)-1
        while l >= f:
            mid = f + (l-f)//2
            
            if target > nums[mid]:
                f = mid + 1
            
            elif target == nums[mid]:
                return mid
            else:
                l = mid -1
                        
        return -1