# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(node, result):
            if not node:
                return False
            
            if not node.left and not node.right:
                if result - node.val == 0:
                    return True 
            
            left = check(node.left, result - node.val)
            right = check(node.right, result - node.val)
            
            return left or right
        
        return check(root, targetSum) 