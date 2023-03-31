class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pref, total = 0, sum(nums) 
        ans = []
        for num in nums: 
            pref += num
            ans.append(abs(total-pref))
            total -= num
        return ans