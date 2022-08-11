class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = len(nums) - 1
        count = 0
        summ = nums[right]
        
        while left >= 0:
            if nums[right] * (right-left+1) > (summ + k):
                
                summ -= nums[right]
                count = max(count, right-left)
                right -= 1
            
            left -= 1
            summ += nums[left]
            
        count = max(count, right-left)
        
        return count

                
        
        