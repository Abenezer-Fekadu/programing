# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        
        ans = []
        queue = [root]
        
        while queue:
            children = []
            lst = []
            for node in queue:
                lst.append(node.val)
                
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            ans.append(lst)
            queue = children
            
        return ans[::-1]