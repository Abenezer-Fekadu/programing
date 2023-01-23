class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(int)
        count = defaultdict(int)
        for a, b in trust:
            graph[a] = b 
            count[b] += 1  

        for i in range(1, n+1):
            if not graph[i] and count[i] == n-1:
                return i

        return -1