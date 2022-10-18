class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def backtrack(lst, i):
            summ = sum(lst)
            if summ >= target:
                if summ == target:
                    ans.add(tuple(lst))
                return
            
            for j in range(i, len(candidates)):
                lst.append(candidates[j])
                backtrack(lst, j)
                lst.pop()
            return
        
        
        backtrack([], 0)
        return ans