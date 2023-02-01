class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        lst = sorted(list(zip(ages, scores)))
        memo = {}
        memo[0] = lst[0][1]
        def helper(i):
            if i not in memo:
                res = 0
                for j in range(i):
                    if lst[i][1] >= lst[j][1]:
                        res = max(res, helper(j))
                memo[i] =  res + lst[i][1]
            return memo[i]
        
        ans = 0
        for i in range(len(ages)):
            ans = max(helper(i), ans)
        return ans
