# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0        
        def dfs(node, count):
            nonlocal ans
            if not node:
                return 0
            
            count ^= (1 << node.val)
            
            left = dfs(node.left, count)
            right = dfs(node.right, count)
            
            if not right and not left:
                if count & (count - 1) == 0:
                    ans += 1
                    
            return 1
                 
        dfs(root, 0)
        return ans
    
    
