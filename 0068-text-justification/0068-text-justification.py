class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        idx = 0
        
        while idx < len(words):
            row = []
            spaces = 0
            j = idx
            
            while idx < len(words) and spaces + len(words[idx]) <= maxWidth:
                spaces += len(words[idx]) + 1
                idx += 1
                
            spaces -= 1 
            num_words = idx - j
      
            spaces_left = maxWidth - spaces
            if num_words == 1:
                row += [words[j], ' '*spaces_left]
                
            else:
                if idx < len(words):
                    extra_spaces= spaces_left // (num_words- 1)
                    num = spaces_left % (num_words-1)
                    for i in range(j, idx):
                        row.append(words[i])
                        spaces_string = ''
                        if i!= idx-1:
                            spaces_string = ' '
                            if extra_spaces > 0:
                                spaces_string += ' '*extra_spaces
                            if i-j < num:
                                spaces_string += ' '
                        row.append(spaces_string)
                else:
                    for i in range(j, idx):
                        row.append(words[i])
                        if i!= idx-1:
                            spaces_string = ' '
                        else:
                            spaces_string = ' '*spaces_left
                            
                        row.append(spaces_string)
            ans.append(''.join(row))
        return ans