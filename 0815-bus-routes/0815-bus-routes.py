class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        graph = defaultdict(set)
        for i in range(len(routes)):
            for j in range(len(routes[i])):
                    graph[routes[i][j]].add(i)
        
        ans = 0
        queue = deque([source])
        while queue:
            for i in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return ans
                
                for bus in graph[stop]:
                    for stops in routes[bus]:
                        queue.append(stops)
                    routes[bus] = []
            
            ans += 1

        return -1