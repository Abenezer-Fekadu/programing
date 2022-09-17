class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            target =- nums[i]
            
            while(l < r):
                summ = nums[l] + nums[r]
                if summ < target:
                    l += 1
                elif summ > target:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    
        return ans