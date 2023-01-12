class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = stones[1]
        for i in range(len(stones) - 2):
            diff = stones[i+2] - stones[i]
            ans = max(ans, diff)

        return ans