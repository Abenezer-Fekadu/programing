class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        left = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                r = mid - 1
                left = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r  = mid - 1
                
        s, e = 0, len(nums) - 1
        right = -1
        while s <= e:
            mid = s + (e-s)//2
            if nums[mid] == target:
                s = mid + 1
                right = mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
                
        return [left, right]
                
                