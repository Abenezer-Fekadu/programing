class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        best = 0
        
        def search(mid):
            count = 0
            for num in candies:
                count += num //mid
            return count
        
        while l <= r:
            mid = l + (r-l)//2
            check = search(mid)
            if check < k:
                r = mid - 1
            else:
                best = mid
                l = mid + 1
                
        return best
                