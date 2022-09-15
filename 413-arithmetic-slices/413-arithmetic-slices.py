class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) < 3:
            return 0
        
        
        diff = nums[1] - nums[0]
        l = 0
        
        for i in range(2, len(nums)):
            if (nums[i] - nums[i-1]) == diff:
                l += 1
                ans += l
            else:
                diff = (nums[i] - nums[i-1])
                l = 0
                
        return ans