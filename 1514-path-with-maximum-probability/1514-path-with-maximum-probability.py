class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(dict)
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            graph[u][v] = (p)
            graph[v][u] = (p)
            
        seen = set()
        distance = [inf for _ in range(n)]
        distance[start] = 0
        q = [(-1, start)]
        
        while q:
            pr, node = heappop(q)
            if node == end:
                return -pr
            
            if node not in seen: 
                seen.add(node) 
                for adj in graph[node]:
                    if adj not in seen:
                        p = graph[node][adj]
                        nxt = pr * p
                        if nxt < distance[adj]:
                            distance[adj] = nxt 
                            heappush(q, (nxt, adj))
                        
        return 0
                    
        
    
                
        
        