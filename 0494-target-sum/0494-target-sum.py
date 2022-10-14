class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(k, num):
            if k == len(nums):
                if num == target:
                    return 1
                return 0
            
            return dp(k+1, num+nums[k]) + dp(k+1, num-nums[k])            
        return dp(0, 0) 
    
    
    
    
    