class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxx = []
        heapify(maxx)
        
        for i in target:
            heappush(maxx, -i)
            
        summ = sum(target)
        while maxx[0] != -1:
            largest = -1*heappop(maxx)
            res = summ - largest
            if summ >= 2*largest or summ == largest:
                return False
            
            previousValue = largest % res
            if previousValue == 0:
                previousValue = res
                
            heappush(maxx, -previousValue)
            summ -= largest
            summ += previousValue
            
        return True