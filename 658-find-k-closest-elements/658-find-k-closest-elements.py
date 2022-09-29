class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1
        summ = 0
        
        for i in range(k):
            summ += abs(x-arr[i])
            
        minn = [summ, l, r]
    
        r += 1
        while r < len(arr):
            summ -= abs(x-arr[l])
            summ += abs(x-arr[r])
            l += 1
            
            if summ < minn[0]:
                minn = [summ, l, r]
                
            r += 1
            
        return arr[minn[1]: minn[2]+1]
            
        
        
        

        
        
        