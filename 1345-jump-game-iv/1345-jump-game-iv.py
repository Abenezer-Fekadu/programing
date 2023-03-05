class Solution:
    def minJumps(self, arr: List[int]) -> int:
        lst = defaultdict(list)
        for i in range(len(arr)):
            lst[arr[i]].append(i)
        
        q = deque([(0, 0)])
        visited = set([0])
        step = float('inf')
        
        while q:
            val = q.popleft()            
            if val[0] == len(arr)-1:
                return val[1]  
            elif arr[val[0]] == arr[-1]:
                step = min(val[1] + 1, step)
             
            left = val[0] - 1 if val[0] - 1 >= 0 else None
            right = val[0] + 1 if val[0] + 1 < len(arr) else None
            
            
            if left and left not in visited:
                q.append((left, val[1]+1))
                visited.add(left)   
            if right and right not in visited:
                q.append((right, val[1]+1))
                visited.add(right)
            for i in lst[arr[val[0]]]:
                if i not in visited:
                    q.append((i, val[1]+1))
                    visited.add(i)
    
            lst[arr[val[0]]] = []
                    
        return step