class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = set()
        for i in range(k, 10):
            if i != 0:
                nums.add(i)
        for j in range(1, 9-k+1):
            nums.add(j)
        
        ans = []
        queue = deque([[i] for i in nums])
        
        while queue:
            top = queue.popleft()
            if len(top) == n:
                ans.append(''.join(map(str, top)))
                continue  
            if top[-1] + k < 10 and k != 0:
                temp1 = top.copy()
                temp1.append(top[-1] + k)
                queue.append(temp1)
            if top[-1] - k >= 0 or k == 0:
                temp2 = top.copy()
                temp2.append(top[-1] - k)
                queue.append(temp2)
            
        
        return ans
        
        