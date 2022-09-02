# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        
        queue = [root]
        while queue:
            children = []
            summ = 0
            for child in queue:
                summ += child.val 
                if child.left: children.append(child.left)
                if child.right: children.append(child.right)
            
            avg  = summ/len(queue)
            ans.append(round(avg, 5))            
            queue = children
            
        return ans
            
                    
            