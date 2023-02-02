class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        op = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                op += 1
                for j in range(i+1, len(nums)):
                    nums[j] = nums[j] - nums[i]
                nums[i] = 0
        return op