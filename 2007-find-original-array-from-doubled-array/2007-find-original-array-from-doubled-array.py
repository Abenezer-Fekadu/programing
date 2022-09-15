class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        
        changed.sort()
        
        check = defaultdict(int)
        for num in changed:
            check[num] += 1
        
        ans = []
        for num in changed:
            if check[num] > 0 and check[2*num] > 0:
                check[num] -= 1
                check[2*num] -= 1
                ans.append(num)
                
        
        for v in check.values():
            if v != 0:
                return []
            
        return ans
            