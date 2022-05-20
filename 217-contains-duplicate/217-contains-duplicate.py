class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return True
            pre = nums[i]
            
        return False