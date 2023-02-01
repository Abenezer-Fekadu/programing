class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:        
        ans = inf
        for i in range(len(blocks)):
            
            op = 0
            t = k
            for j in range(i, i+k):
                if j  >= len(blocks):
                    op = inf
                    break
                if t == 0:
                    break
                elif blocks[j] == 'B':
                    t -= 1
                elif blocks[j] == 'W':
                    op += 1
                    t -= 1
            
            ans = min(ans, op)
        return ans
                
                    