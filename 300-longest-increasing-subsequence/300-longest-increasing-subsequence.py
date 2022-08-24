class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []
        
        def search(num):
            l = 0
            r = len(result) - 1
            best = -1
            
            while l <= r:
                mid = (l+r)//2
                
                if result[mid] >= num:
                    r = mid - 1
                    best = mid
                else:
                    l = mid + 1
            return best
        
        
        
        for num in nums:
            if not result:
                result.append(num)
            elif result[-1] < num:
                result.append(num)
            else:
                val = search(num)
                
                result[val] = num
        return len(result)
                