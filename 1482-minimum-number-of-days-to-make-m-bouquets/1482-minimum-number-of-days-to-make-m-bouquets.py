class Solution:
    def minDays(self, bloomDays: List[int], m: int, k: int) -> int:
        def check(day, m, k, bloomDays):
            count = 0
            for r in range(len(bloomDays)):
                if bloomDays[r] > day:
                    count =  0
                else:
                    count += 1

                if count == k:
                    count = 0
                    m -= 1

            if m <= 0:
                return True
            else:
                return False
            
            
        # best case
        if len(bloomDays)//k < m:
            return -1

        #range for the search
        l, r = min(bloomDays), max(bloomDays)
        ans = r
        while l <= r:
            day = (l+r) // 2

            if check(day, m, k, bloomDays):
                r  = day - 1
                ans = day
            else:
                l = day + 1

        return ans