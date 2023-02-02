class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def check(word1, word2):
            i, j = 0, 0
            while i < len(word1) and j < len(word2):
                if orders[word1[i]] > orders[word2[j]]:
                    return False
                elif orders[word1[i]] < orders[word2[j]]:
                    return True
                i += 1
                j += 1
                
            return len(word1) <= len(word2)
        
        orders = defaultdict(int)
        for i, c in enumerate(order):
            orders[c] = i
            
        for i in range(1, len(words)):
            if not check(words[i-1], words[i]):
                return False
                
        return True
    
    
    
    
