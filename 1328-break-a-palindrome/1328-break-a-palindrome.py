class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
        
        for i in range(((n-1)//2)+1):
            if not palindrome[i] == "a":
                if (not n%2==0) and (i == (n-1)//2):
                    break
               
                return palindrome[:i] + "a" + palindrome[i+1:n] 
        
        return palindrome[0:n-1] + "b"