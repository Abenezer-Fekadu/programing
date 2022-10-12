class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def verify(lst):
            stack = []
            for c in lst:
                if not stack or c == '(':
                    stack.append(c)
                elif stack[-1] == '(' and c == ')':
                    stack.pop()
                else:
                    stack.append(c)
            return len(stack) == 0
        
        ans = set()
        def generate(p):
            if len(p) == n * 2:
                if verify(p):
                    s = "".join(p)
                    ans.add(s)
                return
            
            for i in "()":
                p.append(i)
                generate(p)
                p.pop()
                
        generate(['('])
        return ans
    
   
            