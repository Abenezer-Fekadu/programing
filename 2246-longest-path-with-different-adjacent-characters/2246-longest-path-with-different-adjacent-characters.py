class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(len(s)):
            graph[parent[i]].append((i))

        max_length = 1
        def dfs(i):
            nonlocal max_length
            if not graph[i]:
                return 1

            ans = [0, 0]
            for v in graph[i]:
                res = dfs(v)
                if s[v] != s[i]:
                    ans.append(res)

            ans.sort()
            max_length = max(max_length, ans[-1]+ans[-2]+1)

            return max(ans[-1], ans[-2]) + 1

        dfs(0)
        return max_length 