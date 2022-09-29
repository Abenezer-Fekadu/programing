class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ans =max(ans, i - stack.pop())
        
        
        return ans
            