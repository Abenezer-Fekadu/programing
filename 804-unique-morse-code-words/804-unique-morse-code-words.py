class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
           'a' : ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--.." 
        }
        
        
        count  = 0
        check = {}
        
        for word in words:
            s = []
            for char in word:
                s.append(morse[char])
            
            code = "".join(s)
            if code not in check:
                count += 1
                check[code] = 1
        
        return count