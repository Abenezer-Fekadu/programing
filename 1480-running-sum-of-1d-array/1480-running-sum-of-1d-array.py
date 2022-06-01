class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ, ans = 0,  []
        
        for i in nums:
            summ += i
            ans.append(summ)
            
        return ans