class Solution:
    def isValid(self, s: str) -> bool:
        p = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        stack = []
        for c in s:
            if c in ('(','[','{'):
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                    if p[c] != top:
                        return False
                else:
                    return False
        return len(stack) == 0