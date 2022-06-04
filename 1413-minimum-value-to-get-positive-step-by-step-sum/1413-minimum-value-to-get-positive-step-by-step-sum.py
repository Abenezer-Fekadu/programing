class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n, ans = len(nums), nums[0]
        for i in range(1, n):
            nums[i] += nums[i-1]            
            ans = min(ans, nums[i])
        return -ans + 1 if ans < 0 else 1 
        