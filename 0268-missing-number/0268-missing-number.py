class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            num ^=  i ^ nums[i]
        
        return num ^ (i+1)
        
        
        