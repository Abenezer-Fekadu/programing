class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        new_words =[words[0]]
        for i in range(1, len(words)):
            word1 = ''.join(sorted(words[i]))
            word2 = ''.join(sorted(new_words[-1]))
            
            if word1 == word2:
                  continue
            else:
                new_words.append(words[i])
        
        return new_words
    