# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
#         DFS
        count = 0
        def dfs(node, maxx):
            nonlocal count 
            if not node:
                return 
            
            if node.val >= maxx:
                count += 1
                
            check = max(node.val, maxx)
            left = dfs(node.left, check)
            right = dfs(node.right, check)
        
        dfs(root, root.val)
        return count 
    
#     BFS
#         res = 0
#         queue = deque([[root, root.val]])
#         while queue:
#             node = queue.popleft()
#             if node[0].val >= node[1]:
#                 res += 1
            
#             if node[0].left: queue.append([node[0].left, max(node[1], node[0].left.val)])
#             if node[0].right: queue.append([node[0].right, max(node[1], node[0].right.val)])
    
#         return res
            