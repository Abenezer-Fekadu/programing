# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        def dfs(node, d):
            if not node: return
            
            if d == depth - 1:
                l = TreeNode(val)
                r = TreeNode(val)
                
                node.left, l.left = l, node.left 
                node.right, r.right = r, node.right
                
            left = dfs(node.left, d+1)
            right = dfs(node.right, d+1)
            
            return
        
        
        dfs(root, 1)
        return root
            
            