class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = {}

        for idx, word in enumerate(words):
            if (word[0], word[-1]) in self.trie:
                self.trie[(word[0], word[-1])][word] = idx
            else:
                self.trie[(word[0], word[-1])] = {word: idx}
                
            
    def f(self, prefix: str, suffix: str) -> int:
        size1, size2 = len(prefix), len(suffix)
        ans = -1
        
        if (prefix[0], suffix[-1]) in self.trie:
            for word, index in self.trie[(prefix[0], suffix[-1])].items():
                if word[:size1] == prefix and word[-size2:] == suffix:
                    ans = max(ans, index)
        return ans


        
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)