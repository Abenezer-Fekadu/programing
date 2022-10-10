# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: 
                return 0
            
            right = dfs(node.right)
            ans += node.val
            node.val = ans
            left = dfs(node.left)
    
        
        dfs(root)
        return root