class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp[i] += dp[i-1]
                    
        for j in range(len(arr)-2, -1, -1):
            if arr[j] > arr[j+1]:
                dp[j] += dp[j+1]
        
        ans = 0
        for i, v in enumerate(dp):
            if i != 0 and i != len(dp) -1:
                if arr[i-1] < arr[i] > arr[i+1]: 
                    ans = max(ans, dp[i]) 
                    
        return ans
        