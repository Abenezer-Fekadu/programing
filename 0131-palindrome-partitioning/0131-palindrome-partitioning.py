class Solution:
    def isPalindrom(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(idx, lst):
            if idx == len(s):
                ans.append(tuple(lst))
                return
            
            for i in range(idx, len(s)):
                word = s[idx:i+1]
                if self.isPalindrom(word):
                    lst.append(word)
                    backtrack(i+1, lst)
                    lst.pop()
                    
        backtrack(0, [])
        return ans
        