class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def solve(arr):
            if len(nums) == len(arr):
                ans.add(tuple(arr))
                return
            
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    solve(arr)
                    arr.pop()

        solve([])
        return ans