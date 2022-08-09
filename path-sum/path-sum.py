# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        check = False
        def dfs(node, summ):
            nonlocal check
            if not node:
                return 
            
            if not node.left and not node.right:
                if node.val + summ == targetSum:
                    check = True
                return
            
            dfs(node.left, node.val+summ)
            dfs(node.right, node.val+summ)
        
        
        dfs(root, 0)
        return check