class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q, ans, psum = collections.deque([(-1,0)]), n+1, 0
        for i, a in enumerate(nums):
            psum += a
            if a > 0:
                while q and psum - q[0][1] >= k:
                    ans = min(ans, i-q.popleft()[0])
            else:
                while q and psum <= q[-1][1]:
                    q.pop()
            q.append((i, psum))
        return ans if ans <= n else -1