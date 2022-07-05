class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        pen = 0
        answer = 0
        while pen <= total // cost1:
            val = total - (pen*cost1)
            answer += val // cost2 + 1
            pen += 1
        
        return answer