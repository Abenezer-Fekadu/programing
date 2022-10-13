# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_count = defaultdict(int)
        def dfs(node):
            if not node: return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
      
            cur_sum = left + right + node.val 
            sum_count[cur_sum] += 1
            return cur_sum
        
        dfs(root)
        
        ans = []
        max_count = max(sum_count.values())
        for num in sum_count:
            if sum_count[num] == max_count:
                ans.append(num)
                
        return ans