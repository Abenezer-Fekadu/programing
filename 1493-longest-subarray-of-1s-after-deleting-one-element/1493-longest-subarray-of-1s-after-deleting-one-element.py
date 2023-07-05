class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero, left = 1, 0
        for right in range(len(nums)):
            zero -= nums[right] == 0
            if zero < 0:
                zero += nums[left] == 0
                left += 1

        return right - left