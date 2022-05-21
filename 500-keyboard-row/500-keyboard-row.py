class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rowF = "qwertyuiop"
        rowS = "asdfghjkl"
        rowT = "zxcvbnm"

        for word in words:
            if word[0].lower() in rowF:
                if all(x in rowF for x in word.lower()):
                    ans.append(word)
            elif word[0].lower() in rowS:
                if all(x in rowS for x in word.lower()):
                    ans.append(word)
            elif word[0].lower() in rowT:
                if all(x in rowT for x in word.lower()):
                    ans.append(word)
        return ans