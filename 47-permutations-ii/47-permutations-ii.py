class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def solve(idx, lst):
            if len(lst) == len(nums):
                ans.add(tuple(lst))
                return
            
            for j in range(len(nums)):
                if j not in idx:
                    lst.append(nums[j])
                    idx.append(j)
        
                    solve(idx, lst)
                    
                    lst.pop()
                    idx.pop()
                
            
        solve([], [])
        return ans
            