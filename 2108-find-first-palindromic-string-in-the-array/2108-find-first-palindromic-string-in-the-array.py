class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrom(word):
            right = len(word) - 1
            for left in range(len(word)//2):
                if word[left] != word[right]:
                    return False
                right -= 1
            return True
        
        for word in words:
            if isPalindrom(word):
                return word
            
        return ''