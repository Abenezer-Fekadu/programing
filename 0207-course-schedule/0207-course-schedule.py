class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = {}
        
        for i in range(numCourses):
            indegree[i] = 0
                    
        for j in prerequisites:
            adj[j[1]].append(j[0])
            indegree[j[0]] += 1
        
        queue = []
        for j in indegree:
            if indegree[j] == 0:
                queue.append(j)
        
        count = 0
        while queue:
            val = queue.pop()
            count += 1
            for i in adj[val]:
                if indegree[i] > 0:
                    indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

    
        return count == numCourses
        