class Solution:
    def minimumBuckets(self, street: str) -> int:
        yes, no, lh = inf, 0, inf
        for h in street:
            if h == 'H':
                yes, no, lh = inf, yes, no
            else:
                yes, no, lh = min(lh, no, yes) + 1, min(yes, no), inf
        
        ans = min(yes, no)
        if ans < inf:return ans  
        else: return -1