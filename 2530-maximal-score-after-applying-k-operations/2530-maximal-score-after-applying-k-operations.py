class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        
        ans = 0
        while k > 0:
            val = -heappop(nums)
            
            if not val: return ans
            ans += val
            heappush(nums, -ceil(val/3))
            k -= 1 
            
        return ans
            
        