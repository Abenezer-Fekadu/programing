class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0: return max(nums)
        
        maxx = nums.copy()
        minn = nums.copy()
        
        for i in range(1, len(nums)):
            if maxx[i-1] > 0: maxx[i] += maxx[i-1]
            if minn[i-1] < 0: minn[i] += minn[i-1]
        
        return max(max(maxx),sum(nums) - min(minn))