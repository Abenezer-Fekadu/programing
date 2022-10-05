# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.depthLeft(root.left)
        right = self.depthRight(root.right)
        
        
        if left == right:
            return 2**(left + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def depthLeft(self, node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def depthRight(self, node):
        d = 0
        while node:
            d += 1
            node = node.right
        return d