class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l, r = 0, 0
        check = set()
        while r < len(nums) and l <= r:
            check.add(nums[r])
            if len(check) <= k:
                if r - l + 1 > len(check):
                    return True
                r += 1
            
            else:
                check.remove(nums[l])
                l += 1
                
        return False
    
    
    
    
    