class Solution:
    def removeStars(self, s: str) -> str:
        count  = Counter(s)
        
        stack = []
        i = 0
        while i < len(s):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
            
            count["*"] -= 1
            i += 1
        
        return "".join(stack)
        