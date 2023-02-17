# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = inf
        self.prev = -inf
        def dfs(node):
            if node.left: dfs(node.left)
            
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val

            if node.right: dfs(node.right)

            return node.val

        dfs(root)
        return self.ans