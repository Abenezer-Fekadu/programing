# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         DFS
        check = defaultdict(list)
        def dfs(node, col, row):
            if not node:
                return
            check[col, row].append(node.val)
            check[col, row].sort()
            left = dfs(node.left, col-1, row+1)
            right = dfs(node.right, col+1, row+1)

        dfs(root, 0, 0)
        lst = sorted(check.keys(), key=lambda x: (x[0], x[1]))
        
        
        
        res = defaultdict(list)
        for c, r in lst:
            val = check[(c, r)]
            res[c].extend(val)
        return res.values()
    
    
# BFS
#         check = defaultdict(list)        
#         queue = [(root, 0, 0)]  
#         while queue:
#             node, col, row = queue.pop(0)
#             if not node: continue
#             check[(col, row)].append(node.val)
#             check[(col, row)].sort()
            
#             if node.left: queue.append((node.left, col-1, row+1))
#             if node.right: queue.append((node.right, col+1, row+1)) 
            
            
#         keys = sorted(list(check.keys()), key=lambda x: (x[0], x[1]))
#         res = defaultdict(list)
#         for i in keys:
#             c, r = i
#             res[c].extend(check[i])

#         return res.values()