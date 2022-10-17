class Solution:
    def printVertically(self, s: str) -> List[str]:
        size = 0
        words = s.split()
        for word in words:
            size = max(size, len(word)) 
        ans = ["" for i in range(size)]
        
        for word in words:
            for i in range(size):
                if i < len(word):
                    ans[i] += word[i]
                else:
                    ans[i] += " "
        
        lst = []
        for word in ans:
            t = 0
            for i in range(len(word)-1, -1, -1):
                if word[i] == " ":
                    continue
                else:
                    t = i
                    break
            check = word[:t+1]
            if check:
                lst.append(check)
                
        return lst