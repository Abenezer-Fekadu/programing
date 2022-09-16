class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#         check = {}
#         bound = lambda i: 0 <= i < len(multipliers)
        
#         def helper(index, l):
#             if (index, l) in check:
#                 return check[(index, l)]
            
#             if not bound(index):
#                 return 0

#             left = nums[l]*multipliers[index] + helper(index+1, l+1)
#             right = nums[len(nums) - 1 - (index-l)]*multipliers[index] + helper(index+1, l)
            
#             check[(index, l)] =  max(left, right)
            
#             return check[(index, l)]
        
#         return helper(0, 0)
    
    
    
        check = [0] * (len(multipliers) + 1)
        for m in range(len(multipliers) - 1, -1, -1):
            val = [0] * (m + 1)
            for l in range(m, -1, -1):
                val[l] = max(check[l + 1] + multipliers[m] * nums[l], 
                            check[l] + multipliers[m] * nums[~(m - l)])
            check = val
        return check[0]