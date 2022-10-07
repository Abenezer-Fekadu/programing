class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(i, arr):
            if len(arr) == k:
                ans.append(tuple(arr))
                return
            
            for j in range(i, n+1):
                arr.append(j)
                solve(j+1, arr)
                arr.pop()
            
            return
        
        solve(1, [])
        return ans
            
        