# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        summ = 0
        def dfs(node, num):
            nonlocal summ
            if not node:
                return 
            
            num = num << 1 | node.val
            if not node.left and not node.right:
                summ += num
                return
                
            left = dfs(node.left, num)
            right = dfs(node.right, num)
            return
        
        
        dfs(root, 0)
        return summ
            
            
                    