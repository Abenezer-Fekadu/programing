# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        check = set()
        
        def dfs(node):
            if not node: return False
            
            if node.val in check:
                return True

            check.add(k - node.val)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            
            return left or right
        
        return dfs(root)
        