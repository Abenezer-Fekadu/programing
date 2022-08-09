# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            children = []
            for node in queue:
                if node: 
                    children.append(node.left)
                    children.append(node.right)

            l = 0
            r = len(children) -1 
            
            while l < r:
                if children[l] and children[r]:
                    if children[l].val != children[r].val:
                        return False
                elif children[l]  or children[r]:
                    return False
                
                l += 1
                r -= 1
            
            
            queue = children
            
        return True
                
            