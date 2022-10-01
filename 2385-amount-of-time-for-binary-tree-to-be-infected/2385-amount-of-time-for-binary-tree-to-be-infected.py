# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        tree = defaultdict(list)
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.left:
                tree[node.val].append(node.left.val)
                tree[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                tree[node.val].append(node.right.val)
                tree[node.right.val].append(node.val)
                stack.append(node.right)

                
        visited = {start}
        queue = [start]
        depth = [0]
        for node, d in zip(queue, depth):
            for child in tree[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
                    depth.append(d + 1)
        
        return depth[-1]