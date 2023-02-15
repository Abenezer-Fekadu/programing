class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        
        def backtrack(prev, curr):
            if not curr:
                return 1

            ans = 0
            for i, num in enumerate(curr):
                temp = curr[:i] + curr[i+1:]
                if i > 0 and curr[i-1] == num or (prev != -1 and math.sqrt(prev+num)%1 != 0):
                    continue
        
                ans += backtrack(num, temp)
                
            return ans     
        return backtrack(-1, nums)