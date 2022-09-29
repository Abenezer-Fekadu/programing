class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        
        for i in range(k-1):
            if not queue:
                queue.append(nums[i])
            else:
                while queue and queue[-1] < nums[i]:
                    top = queue.pop()
                
                queue.append(nums[i])
                
        r = k-1
        answ = []
        while r < len(nums):
            while queue and queue[-1] < nums[r]:
                queue.pop()
                
            queue.append(nums[r])
            r += 1
            
            
            answ.append(queue[0])
            if nums[r-k] == queue[0]:
                queue.popleft()
            
            
        return answ