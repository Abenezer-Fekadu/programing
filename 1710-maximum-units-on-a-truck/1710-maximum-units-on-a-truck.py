class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        ans = 0
        for i in range(len(boxTypes)):
            val = truckSize - boxTypes[i][0]  
            if val > 0:
                ans += (boxTypes[i][0]*boxTypes[i][1])
                truckSize -= boxTypes[i][0]
            else:
                if truckSize < 0:
                    break
                ans += (truckSize*boxTypes[i][1])
                truckSize -= boxTypes[i][0]
                
        return ans