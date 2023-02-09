class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        
        l, r = 0, 0
        ans = 0
        for num in nums:
            window[num] += 1
            if len(window) >= k:
                while len(window) > k:
                    window[nums[r]] -= 1
                    if window[nums[r]] == 0:
                        del window[nums[r]]
                    r += 1
                    l = r
         
                while window[nums[r]] - 1 > 0:
                    window[nums[r]] -= 1
                    r += 1
                
                ans += (r - l + 1)
        
        return ans