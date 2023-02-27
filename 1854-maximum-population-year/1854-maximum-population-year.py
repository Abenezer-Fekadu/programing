class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        vals = []
        for b, d in logs: 
            vals.append((b, 1))
            vals.append((d, -1))
            
            
        ans, count, = 0, 0
        maxx = 0
        for year, v in sorted(vals): 
            count += v
            if count > maxx: 
                maxx = count 
                ans = year
                
        return ans