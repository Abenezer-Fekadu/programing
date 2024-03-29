class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        def find(x):
            parent.setdefault(x,x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX>rootY:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        res = []
        for c in baseStr:
            res.append(find(c))
            
        return ''.join(res)