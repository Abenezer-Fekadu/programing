class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size = len(words[0])
        wlen = len(words) * len(words[0])
        ans = []
        
        for pos in range(size):
            i = pos
            count = Counter(words)
            
            for j in range(i, len(s) + 1 - size, size):
                word = s[j: j + size]
                count[word] -= 1
                
                while count[word] < 0:
                    count[s[i: i + size]] += 1
                    i += size
                if i + wlen == j + size:
                    ans. append(i)
        
        return ans