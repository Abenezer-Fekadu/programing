class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        count_words = defaultdict(list)
        matched = 0 

        for word in words:
            count_words[word[0]].append(word)
        
        for c in s:
            words = count_words[c]
            del count_words[c]
            
            for word in words:
                if len(word) == 1:
                    matched += 1
                else:
                    count_words[word[1]].append(word[1:])
        
        return matched
    
    
    
    
    

    
    
    