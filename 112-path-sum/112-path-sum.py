# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        def dfs(node, summ):
            if not node:
                return False
            if not node.left and not node.right:
                if node.val + summ == targetSum:
                    return True
            
            left =  dfs(node.left, node.val+summ)
            right = dfs(node.right, node.val+summ)
        
            return left or right
        
        return dfs(root, 0)