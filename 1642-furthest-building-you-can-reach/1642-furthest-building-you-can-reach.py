class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        lst = []
        count = 0
        for i in range(len(heights)-1):
            
            diff = heights[i+1] - heights[i]
                       
            if heights[i] > heights[i+1]:
                count += 1
                continue
                
            if len(lst) < ladders:
                heappush(lst, diff)
               
            else:                
                val = heappushpop(lst, diff)
                if val <= bricks:
                    
                    bricks -= val
                    count += 1

                else:
                    break
                                      
      
        return count + len(lst)