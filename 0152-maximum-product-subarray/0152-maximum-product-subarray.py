class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        maxProduct = 1
        minProduct = 1
        for i in nums:
            if i != 0:
                temp = [i, i*minProduct, i*maxProduct]
                maxProduct = max(temp)
                minProduct = min(temp)
                ans = max(ans, maxProduct)
            else:
                minProduct = 1
                maxProduct = 1
                
            
        return ans
        
