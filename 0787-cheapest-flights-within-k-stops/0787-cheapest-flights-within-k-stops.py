class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for f, t, p in flights:
            graph[f][t] = p
        
        
        queue = [(0, k, src)]
        distance = [inf for _ in range(n+1)]
        stops = [inf for _ in range(n+1)]

        distance[src] = 0
        
        while queue:
            cost , steps , node = heappop(queue)    
            if steps < -1: continue
            if node == dst: return cost

            for neighbour in graph[node]:
                nxt = cost + graph[node][neighbour]
                if nxt < distance[neighbour] or steps - 1 > stops[neighbour]:
                    distance[neighbour] = nxt
                    stops[neighbour] = steps - 1
                    heappush(queue, (nxt, steps-1, neighbour))
                    
        return -1
                        
        