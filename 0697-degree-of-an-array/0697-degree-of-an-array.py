class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        ans = inf
        count, d = defaultdict(list), 0
        for i, num in enumerate(nums):
            count[num].append(i)
            if len(count[num]) == d:
                ans = min(ans, count[num][-1] - count[num][0] + 1)
            elif len(count[num]) > d:
                ans = count[num][-1] - count[num][0] + 1
                d = len(count[num])
                
        return ans