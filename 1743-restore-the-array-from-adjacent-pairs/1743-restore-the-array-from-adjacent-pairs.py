class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        start = 0
        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break
        
        ans = []
        seen = set([start])
        queue = [start]
        while queue:
            num = queue.pop(0)
            ans.append(num)
            for adj in graph[num]:
                if adj not in seen:
                    seen.add(adj)
                    queue.append(adj)
                    
        return ans
        
        
        