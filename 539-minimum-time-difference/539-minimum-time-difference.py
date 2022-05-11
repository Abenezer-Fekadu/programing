class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        ft = timePoints[0].split(":")
        sd = timePoints[1].split(":")
        
        dif = (int(sd[0])*60 + int(sd[1])) - (int(ft[0])*60 + int(ft[1]))
        for i in range(2, len(timePoints)):
            lst = timePoints[i].split(":")
            minute2 = int(lst[0])*60 + int(lst[1])
            minute = int(sd[0])*60 + int(sd[1])
 
            dif = min(dif, minute2 - minute)
            sd = timePoints[i].split(":")
    
            
        last = timePoints[-1].split(":")
        check = (24*60 - (int(last[0])*60 + int(last[1])) + (int(ft[0])*60 + int(ft[1])))
        
        dif = min(check, dif)
        
        
        return dif

        