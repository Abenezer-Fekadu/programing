class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            l = str(sorted(s))
            anagram[l].append(s)
        
        return list(anagram.values())
                
                