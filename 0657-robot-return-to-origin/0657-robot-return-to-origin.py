class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {}
        for m in moves:
            d[m] = d.get(m, 0)+1
        
        if(d.get("U",0) == d.get("D",0) and d.get("L",0) == d.get("R",0)):
            return True
        return False