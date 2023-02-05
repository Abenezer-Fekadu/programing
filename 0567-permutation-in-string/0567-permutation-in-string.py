class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count, size = Counter(s1), len(s1)   
        for i in range(len(s2)):
            if s2[i] in count: 
                count[s2[i]] -= 1
            if i >= size and s2[i-size] in count: 
                count[s2[i-size]] += 1

            if all([count[i] == 0 for i in count]): 
                return True

        return False

