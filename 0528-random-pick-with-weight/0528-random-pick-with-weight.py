class Solution:

    def __init__(self, w: List[int]):
        self.weights = list(accumulate(w))
    
    def pickIndex(self):
        choice = randint(1, self.weights[-1])
        
        best = 0
        l, r = 0, len(self.weights)-1
        while l < r:
            mid = l + (r-l)//2
            if choice > self.weights[mid]:
                l = mid + 1
                best = l
            else:
                r = mid
                
        return best
    
    

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()