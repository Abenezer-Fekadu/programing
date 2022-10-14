class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        ans = []
        while queue:
            top = queue.popleft()
            ans.append(top)
            for pre in graph[top]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
          
        for v in indegree.values():
            if v != 0:
                return []
            
        return ans