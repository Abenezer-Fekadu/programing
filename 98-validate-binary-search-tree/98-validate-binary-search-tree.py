# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        num = float("-inf")
        ans = True
        def dfs(node):
            nonlocal num, ans
            if node:            
                dfs(node.left)
                if num >= node.val:
                    ans = False
                    return
                    
                num = node.val
                dfs(node.right)
                
            return
        dfs(root)
        return ans