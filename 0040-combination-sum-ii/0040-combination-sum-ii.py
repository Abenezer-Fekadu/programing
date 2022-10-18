class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        
        def dfs(i, lst, targetTillNow):
            if targetTillNow <= 0:
                if targetTillNow == 0:
                    ans.append(tuple(lst))
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                lst.append(candidates[j])
                dfs(j+1, lst, targetTillNow - candidates[j])
                lst.pop()
        
        dfs(0, [], target)
        return ans