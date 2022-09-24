# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node, running_sum, arr):
            if not node:
                return
                        
            arr.append(node.val)
            running_sum += node.val
            
            if not node.left and not node.right:
                if running_sum == targetSum:
                    ans.append(list(arr))
                    
                arr.pop()
                return
            
            dfs(node.left, running_sum, arr)
            dfs(node.right, running_sum, arr)
            arr.pop()
            
        dfs(root, 0, [])
        return ans