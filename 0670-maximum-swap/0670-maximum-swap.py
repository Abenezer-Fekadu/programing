class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        
        check = True
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                check = False
                break
        if check:
            return num
        
        max_idx = i       
        for i in range(i, len(nums)):
            if nums[i] >= nums[max_idx]:
                max_idx = i
               
        for i in range(max_idx):
            if nums[i] < nums[max_idx]:
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
                break
        
        return int(''.join(nums))
                
    
    