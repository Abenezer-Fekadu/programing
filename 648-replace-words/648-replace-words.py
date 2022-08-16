class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
            
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
            
        cur.isWord = True
        

    def search(self, word: str):
        cur = self.root
        s = []
        for c in word:
            
            if c in cur.children:
                cur = cur.children[c]
                s.append(c)
            else:
                return []
                
            if cur.isWord:
                return "".join(s)
                
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        node = Trie()
        for word in dictionary:
            node.insert(word)
        
        lst = sentence.split()
        
        ans = []
        for word in lst:
            val = node.search(word)
            if val:
                ans.append(val) 
            else:
                ans.append(word)
        
        return " ". join(ans) 
            
        