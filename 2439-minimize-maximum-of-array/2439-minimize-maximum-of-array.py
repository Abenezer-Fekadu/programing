class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans, pref = 0, 0
        for i in range(len(nums)):
            pref += nums[i]
            ans = max(ans, (pref+i)//(i+1))
        return ans