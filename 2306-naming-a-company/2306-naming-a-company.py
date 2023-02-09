class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        names = defaultdict(set)
        for w in ideas:
            names[w[0]].add(w[1:])
        
        ans = 0
        for char1 in names:
            for char2 in names:
                if char1 != char2:
                    intersect = 0
                    for w in names[char1]:
                        if w in names[char2]:
                            intersect += 1

                    distinct1 = len(names[char1]) - intersect
                    distinct2 = len(names[char2]) - intersect

                    ans += distinct1*distinct2
        return ans