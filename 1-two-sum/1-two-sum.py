class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for j in range(len(nums)):
            check[nums[j]] = j
            
        for i in range(len(nums)):
            val = target - nums[i]
            if check.get(val) and check.get(val) != i:
                return [check[val], i]
                