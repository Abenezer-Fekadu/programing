class Solution:
    def myAtoi(self, s: str) -> int:                
        ans = []
        op = ""
        for i in range(len(s)):
            if s[i].isalpha() or (s[i] == " " and (op or ans)):
                break
            elif s[i] in "-+":
                if op or ans:
                    break
                op = s[i]
            else:
                if s[i] == " ":
                    continue
                ans.append(s[i])
                
        if not ans:
            return 0
        num = 0 - float("".join(ans)) if op == '-' else float("".join(ans))

        if num >= 2**31 - 1:
            return 2**31 - 1
        elif num <= -2**31:
            return -2**31
        
        return int(num)
            
        
        