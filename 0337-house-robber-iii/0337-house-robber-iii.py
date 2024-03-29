# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node: 
                return (0, 0)
        
            left = solve(node.left)
            right = solve(node.right)

            return (max(left) + max(right), node.val + left[0]+ right[0])
        
        return max(solve(root))                    
        