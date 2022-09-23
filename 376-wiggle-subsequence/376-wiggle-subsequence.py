class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 1
        prev = 0
        for i in range(1, len(nums)):
            temp = nums[i] - nums[i-1] 
            if (temp > 0 and prev < 0) or (prev > 0 and temp < 0) or (prev == 0 and temp != 0):
                count += 1
            else:
                continue
                
            prev = temp         
        return count
    
    
    