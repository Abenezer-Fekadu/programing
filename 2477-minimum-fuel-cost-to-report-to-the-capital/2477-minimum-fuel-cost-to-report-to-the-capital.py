class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for u ,v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        ans = 0
        def dfs(node, par):
            nonlocal ans
            totalPeople = 1
            for adj in graph[node]:
                if adj != par:
                    people, car = dfs(adj, node)
    
                    totalPeople += people
                    
                    ans += car

            cars = ceil(totalPeople/seats)
            
            return totalPeople, cars

        dfs(0, None)
        return ans