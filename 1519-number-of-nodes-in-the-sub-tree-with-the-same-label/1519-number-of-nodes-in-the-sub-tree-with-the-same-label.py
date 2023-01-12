class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set([0])
        ans = [0] * n
        def dfs(node):
            if not graph[node]: return {}
            
            temp = []
            for adj in graph[node]:
                if adj not in seen:
                    seen.add(adj)
                    temp.extend(dfs(adj).items())
            
            res = defaultdict(int)
            res[labels[node]] += 1
            for k, v in temp:
                res[k] += v
            
            ans[node] =  res[labels[node]]
            return res
    
        dfs(0)
        return ans
                