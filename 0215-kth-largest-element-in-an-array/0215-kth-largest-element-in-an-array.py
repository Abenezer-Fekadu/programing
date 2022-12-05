class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot = nums[r]
            i = l - 1
            for j in range(l, r):
                if nums[j] <= pivot:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[i+1], nums[r] = nums[r], nums[i+1]
            
            return i + 1
            
            
        def quick_select(l, r):
            idx = partition(l, r)
            if idx == k:
                return nums[idx]
            elif idx > k:
                return quick_select(l, idx-1)
            else:
                return quick_select(idx+1, r)

        
        k = len(nums) - k
        return quick_select(0, len(nums)-1)
      
        
        