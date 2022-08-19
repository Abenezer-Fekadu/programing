class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def search(mid):
            hours = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    hours += 1
                else:
                    num = piles[i]//mid
                    hours += num
                    if piles[i]%mid:
                        hours += 1
            
            return hours
        
            
        left = 1
        right = max(piles)
        best = left
        
        while left <= right:
            mid = left + (right-left)//2
            
            if search(mid) > h:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        
        return best
                
            