class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = {}
        
        def calculate(num):
            if num >= len(cost) - 2:
                return cost[num]
            
            if num in stairs:
                return stairs[num]
            
            stairs[num] = cost[num] + min(calculate(num+1), calculate(num+2))
            return stairs[num]
        
        return min(calculate(0), calculate(1))