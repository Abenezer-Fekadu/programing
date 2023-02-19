# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        level = deque([root])
        ans = []
        ans.append([root.val])
        count = 0
        while level:
            for i in range(len(level)):
                node = level.popleft()
                if node:
                    level.append(node.left)
                    level.append(node.right)
                    
            if level:
                count += 1
            
            
            rev = []
            if count % 2 != 0:
                for i in range(len(level)-1, -1, -1):
                    if level[i]:
                        rev.append(level[i].val)
                if rev != []: ans.append(rev)
            else:
                for i in range(0, len(level)):
                    if level[i]:
                        rev.append(level[i].val)
                if rev != []: ans.append(rev)

        return ans