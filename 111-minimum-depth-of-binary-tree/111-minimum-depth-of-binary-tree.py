# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
                
        def dfs(node, count):
            if node:
                if not node.left and not node.right:
                    return count
                if not node.left:
                    return dfs(node.right, count + 1)
                if not node.right:
                    return dfs(node.left, count + 1)
                
                right = dfs(node.right, count + 1)
                left = dfs(node.left, count + 1)
                
                return min(left,right)
            
        return dfs(root, 1) if root else 0
            