class Solution:
    def decodeString(self, s: str) -> str:
        prev = 0
        def recurse(i, strs):
            nonlocal prev
            if i == len(s):
                return ""
            
            if s[i] == "]":
                prev = i 
                return ""
			
            if s[i] == "[":
                return int(strs)*recurse(i+1,"") + recurse(prev+1, "")
				
            if s[i].isnumeric():
                return recurse(i+1, strs+s[i])
            else:
                return s[i] + recurse(i+1, strs)
				
        return recurse(0, "")
    