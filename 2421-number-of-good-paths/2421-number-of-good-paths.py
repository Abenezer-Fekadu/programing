class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        parent = [num for num in range(n)]
        count = [Counter({vals[i]:1}) for i in range(n)]
        edges = sorted((max(vals[u], vals[v]), u, v) for u, v in edges)
        
        res = n
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        
        for val, u, v in edges:
            root1, root2 = find(u), find(v)
            res += count[root1][val] * count[root2][val]
            parent[root1] = root2
            count[root2][val] += count[root1][val]
            
        return res