# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node: return 0, 0
            
            left, left_count = dfs(node.left)
            right, right_count = dfs(node.right)
            
            summ = node.val + left + right
            
            num = 1 + left_count + right_count
            if summ // num == node.val:
                count += 1
            
            return summ, num
        
        
        dfs(root)
        return count