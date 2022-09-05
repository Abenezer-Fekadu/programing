"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        ans = []
        while queue:
            children = []
            for i in range(len(queue)):
                node = queue.pop(0)
                children.append(node.val)
                
                queue.extend(node.children)
            
            ans.append(children)
                
        return ans