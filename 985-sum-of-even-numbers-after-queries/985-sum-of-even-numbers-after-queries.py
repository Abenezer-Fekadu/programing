class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = 0
        ans = []
        for num in nums:
            if num % 2 == 0:
                summ += num
                
        for query in queries:
            v, i = query 
            if nums[i] % 2 == 0:
                summ -= nums[i]
            
            nums[i] += v
            if nums[i] % 2 == 0:            
                summ += nums[i]
                   
            ans.append(summ)
            
        return ans    
    
    