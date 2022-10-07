class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(i, arr):
            if i == len(graph) - 1:
                ans.append(tuple(arr))
                return
                
            for j in graph[i]:
                arr.append(j)
                dfs(j, arr)
                arr.pop()
      
        dfs(0, [0])
        return ans