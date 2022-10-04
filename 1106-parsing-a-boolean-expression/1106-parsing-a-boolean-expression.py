class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        op = { '&': all, '|': any, '!': lambda x: not x[0], 'f': False, 't': True, "(": '('}

        stack = []
        for c in expression:
            if c in op:
                stack.append(op[c])
                
            elif c == ')':
                temp = []
                while stack[-1] != '(':
                    val = stack.pop()
                    temp.append(val)
                    
                stack.pop()
                stack.append(stack.pop()(temp))
                            
        return stack[0]
        