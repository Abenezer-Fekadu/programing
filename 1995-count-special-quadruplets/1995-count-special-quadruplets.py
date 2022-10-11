class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count, n = 0, len(nums)
        leftVal = Counter()
        for c in range(2, n):
            b = c - 1
            for a in range(0, b):
                leftVal[nums[a]+nums[b]] += 1
                
            for d in range(c+1, n):
                count += leftVal[nums[d]-nums[c]]
                
        return count