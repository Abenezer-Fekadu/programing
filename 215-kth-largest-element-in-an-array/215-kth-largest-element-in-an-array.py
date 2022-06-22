class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return nlargest(k, nums)[-1]
    
        lst = [-1*i for i in nums]
        
        heapify(lst)
        for i in range(k-1):
            heappop(lst)
            
        return -1*lst[0]