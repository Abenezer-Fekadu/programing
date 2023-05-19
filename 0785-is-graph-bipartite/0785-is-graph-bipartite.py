class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, color):
            if visited[node] == 1:
                visited[node] = color
        
            for i in graph[node]:
                if visited[i] == 1:
                    dfs(i, not color)
                else:
                    if visited[i] == (color):
                        ans[0] = False
                        return
        
        
        visited = [1 for i in range(len(graph))]
        ans = [True]
        for j in range(len(graph)):
            if visited[j] == 1:
                dfs(j, True)
                
        return ans[0]