class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        rank = [1] * size
        root = [i for i in range(size)]
        
        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    root[root2] = root1
                elif rank[root1] < rank[root2]:
                    root[root1] = root2
                else:
                    root[root2] = root1
                    rank[root1] += 1

        
        for i in range(size):
            for j in range(size):
                if isConnected[i][j]:
                    union(i, j)

        res = 0
        for i in range(size):
            if root[i] == i:
                res += 1
        return res