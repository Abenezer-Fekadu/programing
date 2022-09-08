class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        rob = {}
        def robber(index, last):
            l, r = 0, 0
            for i in range(index, last):
                l, r = max(l, r + nums[i]), l
            
            return l
        
        return max(robber(0, len(nums) -1), robber(1, len(nums)))
    
    