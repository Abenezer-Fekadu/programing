class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        nums = list(set(nums))
        
        def partition(l, r):
            pivot = freq[nums[r]]
            i = l
            for j in range(l, r):
                if freq[nums[j]] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        def quick_select(l, r):
            if l > r:
                return nums[:l]
            
            idx = partition(l, r)
            if idx == k:
                return nums[:k]
            elif idx > k:
                return quick_select(l, idx-1)
            else:
                return quick_select(idx+1, r)
            
        return quick_select(0, len(nums)-1)