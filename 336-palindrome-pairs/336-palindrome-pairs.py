class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        check = {}
        res = []
        for i, word in enumerate(words):
            check[word[::-1]] = i
            
        for i, word in enumerate(words):
            if word != "" and "" in check and word == word[::-1]:
                res.append([i, check[""]])
                res.append([check[""], i])
                
            if word in check and check[word] != i:
                res.append([i, check[word]])
                
            for j in range(len(word)):
                if word[j:] in check and word[:j] == word[j-1::-1]:
                    res.append([check[word[j:]], i])
                if word[:j] in check and word[j:] == word[:j-1:-1]:
                    res.append([i, check[word[:j]]])
                    
                    
        return res