class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        stack = []
        
        for i in reversed(range(len(nums))):
            if not stack or stack[-1] <= nums[i]:
                stack.append(nums[i])
            else:            
                for j in range(len(stack)):
                    if stack[j] > nums[i]:
                        nums[i], stack[j] = stack[j], nums[i] 
                        break

                l = 0
                r = i + 1
                while r < len(nums):
                    nums[r] = stack[l]
                    l += 1
                    r += 1
                return
            
        nums.reverse()