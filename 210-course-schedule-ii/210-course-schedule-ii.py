class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        res = []
        indegree = {}
        
        for i in range(numCourses):
            indegree[i] = 0
            
        for i in prerequisites:
            adj[i[1]].append(i[0])
            indegree[i[0]] += 1
        
        queue = []
        for j in indegree:
            if indegree[j] == 0:
                queue.append(j)
                
        while queue:
            val = queue.pop(0)
            res.append(val)
            for i in adj[val]:
                if indegree[i] > 0:
                    indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        for i in indegree:
            if indegree[i] != 0:
                return []
            
        return res
