class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = {}
        for num in nums:
            table[num] = 1
            
        for i in range(1, len(nums)+2):
            if not table.get(i):
                return i
            
        return len(nums)