class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums = [1] + nums + [1]
        memo = defaultdict(int)
        def dp(i, j):
            if i > j: 
                return 0 
            if (i, j) not in memo:                            
                ans = 0
                for k in range(i, j+1):
                    c = nums[k]*nums[i-1]*nums[j+1]
                    ans = max(ans, c + dp(k+1, j) + dp(i, k-1))

                memo[(i, j)] = ans
            return memo[(i, j)]
        
        return dp(1, len(nums)-2)