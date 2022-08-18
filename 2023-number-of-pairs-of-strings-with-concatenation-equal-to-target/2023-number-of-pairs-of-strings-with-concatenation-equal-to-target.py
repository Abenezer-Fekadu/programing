class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                val = nums[i] + nums[j]
                if val == target and i != j:
                    count += 1
        return count