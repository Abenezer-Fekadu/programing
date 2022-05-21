class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rowF = "QqWwEeRrTtYyUuIiOoPp"
        rowS = "AaSsDdFfGgHhJjKkLl"
        rowT = "ZzXxCcVvBbNnMm"

        for word in words:
            f = [word[i] in rowF for i in range(len(word))]
            s = [word[i] in rowS for i in range(len(word))]
            t = [word[i] in rowT for i in range(len(word))]

            if all(f) or all(s) or all(t):
                ans.append(word)

        return (ans)