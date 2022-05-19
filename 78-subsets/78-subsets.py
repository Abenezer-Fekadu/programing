class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, N = [], len(nums) 
        for i in range(2 ** N): 
            subset, j = [], 0 
            while i: 
                if i & 1: 
                    subset.append(nums[j])
                i = i >> 1 
                j+= 1 
            ans.append(subset) 
        return ans
    