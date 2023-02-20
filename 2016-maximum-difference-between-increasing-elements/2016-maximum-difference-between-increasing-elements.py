class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                diff = nums[j] - nums[i] 
                if diff > ans and diff != 0:
                    ans = nums[j] - nums[i]
        return ans