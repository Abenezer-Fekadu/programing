class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxx = 0
        summ = defaultdict(int)
        for num in nums:
            summ[num] += num
            maxx = max(maxx, num)

        def calculate(i):
            if i == 0:
                return 0
            if i == 1:
                return summ[i]
            if i not in memo:
                memo[i] = max(calculate(i-1), calculate(i-2) + summ[i]) 
            return memo[i]
        
        memo = {}
        return calculate(maxx)