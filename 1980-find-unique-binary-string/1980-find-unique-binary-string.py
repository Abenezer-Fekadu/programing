class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        #         backtrack function
        def backtrack(s):
            # base case to return, len(arr) == n
            if len(s) == len(nums):
                m = "".join(s)
                if m not in nums:
                    ans.append(m)
                return
                
            
            # loop and apdate array
            for c in "01":
                s.append(c)
                backtrack(s)
                s.pop()
        
        backtrack([])
        return ans[0]