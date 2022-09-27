class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = min(height[l], height[r]) * (r-l)
    
        while l < r:
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
                
            curr = min(height[l], height[r]) * (r - l)            
            ans = max(ans, curr)
            
        return ans