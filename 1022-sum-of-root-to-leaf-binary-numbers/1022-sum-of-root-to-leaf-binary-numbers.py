# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        summ = 0
        
        def dfs(node, s):
            nonlocal summ
            if not node:
                return 
            
            num = s + str(node.val)
            if not node.left and not node.right:
                ans = 0
                for i in range(len(num)):
                    ans = (ans << 1)
                    ans = (ans | int(num[i]))
                    
                summ += ans
                
            left = dfs(node.left, num)
            right = dfs(node.right, num)
            return
        
        
        dfs(root, "")
        return summ
            
            
                    