# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:   
        def search(l, size1, r, size2):
            if r > size2:
                return None
            
            num = preorder[l]
            index = inorder.index(num)
            node = TreeNode(
                num, 
                search(l + 1, l + index - r, r, index - 1),
                search(l + 1 + index - r, size1, index + 1, size2),
            )
            
            return node

        return search(0, len(preorder) - 1, 0, len(inorder) - 1)