class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        while r < len(nums) - 1:
            maxx = 0
            for i in range(l, r+1):
                maxx = max(nums[i] + i, maxx)
            
            l = r + 1
            r = maxx
            count += 1
        
        return count
        