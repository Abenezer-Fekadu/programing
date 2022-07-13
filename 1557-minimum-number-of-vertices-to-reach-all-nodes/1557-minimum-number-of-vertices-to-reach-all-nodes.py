class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        lst = [-1]*(n)
        for i in edges:
            lst[i[1]] = 0
            
            
        ans = []
        for j in range(n):
            if lst[j] == -1:
                ans.append(j)
                
        return ans
            