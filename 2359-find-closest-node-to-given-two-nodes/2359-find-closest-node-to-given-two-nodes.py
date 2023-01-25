class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        queue = [(node1, 1),(node2, 2)] 
        seen = [0]*(len(edges))
        ans = inf
        while queue:  
            temp = []
            check = False
            for node, d in queue:
                if not seen[node]:
                    if edges[node] != -1:
                        temp.append((edges[node], d))
                    seen[node] = d
                    
                elif seen[node] != d:
                    check = True
                    ans = min(node, ans)        
            if check:
                return ans       
            queue = temp 
        return -1