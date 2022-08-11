# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        num = float("-inf")
        def dfs(node):
            nonlocal num
            if not node:
                return True
            
            left = dfs(node.left)
            if num >= node.val:
                return False
            
            num = node.val
            right = dfs(node.right)

            return left and right
        return dfs(root)