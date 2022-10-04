class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s =  target - nums[j] - nums[i]
                l, r = j+1, len(nums) - 1
                while l < r:
                    summ = nums[l] + nums[r] 
                    if summ == s:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    elif summ < s:
                        l += 1
                    else:
                        r -= 1
        return ans