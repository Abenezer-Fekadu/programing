class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            if vals[u] > 0 : graph[v].add(u)
            if vals[v] > 0 : graph[u].add(v)
            
            
        ans = []
        for u, v in enumerate(vals):
            values = [vals[adj] for adj in graph[u]]
            values.sort(reverse=True)
            ans.append(v + sum(values[0:k]))
            
        return max(ans)