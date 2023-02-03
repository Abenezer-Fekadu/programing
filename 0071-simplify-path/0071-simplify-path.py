class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        paths = []
        for p in path:
            if p != "" and p != ".":
                paths.append(p)
        
        ans = "/"
        stack = []
        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
                
        return ans + "/".join(stack)