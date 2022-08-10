class Solution:
    def countAndSay(self, n: int) -> str:
        s = ['1']
        for i in range(1, n):
            count = 1
            child = []
            prev = s[0]
            for j in range(len(s)):
                if j+1 < len(s) and s[j] == s[j+1]:
                    count += 1
                else:
                    prev = s[j] 
                    child.append(str(count))
                    child.append(s[j])
                    count = 1
                    
            if prev != s[-1]:
                child.append(str(count))
                child.append(s[-1])
            
            s = child if child else s
            
        return "".join(s) 