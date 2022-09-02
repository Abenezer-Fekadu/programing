class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        adj = defaultdict(list)
        rest = set(restricted)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
         
        count = 1
        queue = deque(adj[0])
        rest.add(0)
        while queue:
            node = queue.popleft()
            if node not in rest:
                rest.add(node)
                count += 1
                for i in adj[node]:
                    if i not in rest:
                        queue.append(i)
        
        return count
            