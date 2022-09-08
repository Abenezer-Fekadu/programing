class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = {}  
        def robber(index):
            if len(nums) <= index:
                return 0
            if index not in rob:
                rob[index] = nums[index]  + max(robber(index + 2), robber(index + 3))
                
            return rob[index]

        return max(robber(0), robber(1))
        