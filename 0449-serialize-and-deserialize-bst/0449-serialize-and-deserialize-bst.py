# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def ser(node):
            if not node: return node
            
            ans.append(str(node.val))
            if node.left:
                ans.append('(')
                ser(node.left)
                ans.append(')')
            if node.right:
                if not node.left: ans.append('()')
                ans.append('(')
                ser(node.right)
                ans.append(')')
            
        ser(root)  
        return "".join(ans)
        

    def deserialize(self, s: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def dfs(i):
            if i >= len(s):
                return None

            cur = ""
            while i < len(s) and s[i] not in '()':
                cur += s[i]
                i += 1
                
            node = None
            if cur:
                node = TreeNode(cur)
            if i < len(s) and s[i] == '(':
                i += 1
                node.left, i = dfs(i)
                i += 1
                if i < len(s) and s[i] == '(':
                    i += 1
                    node.right, i = dfs(i)
                    i += 1

            return node, i

        ans = dfs(0)
        return ans[0] if ans else []

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans