# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def dfs(node):
            if not node: return
            
            ans.append(str(node.val))
            if node.left:
                ans.append('(')
                dfs(node.left)
                ans.append(')')
            if node.right:
                if not node.left: ans.append("()")
                ans.append('(')
                dfs(node.right)
                ans.append(')')
            return

        dfs(root)
        return "".join(ans)
    
    
    