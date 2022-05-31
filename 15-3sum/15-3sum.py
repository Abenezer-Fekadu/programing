class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            start = i+1
            finish = len(nums)-1
            target =- nums[i]
            
            while(start < finish):
                summ = nums[start] + nums[finish]
                if summ < target:
                    start += 1
                elif summ > target:
                    finish -= 1
                else:
                    res.add((nums[i], nums[start], nums[finish]))
                    start += 1
                    finish -= 1
        return res