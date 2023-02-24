class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        freq = defaultdict(set)
        for i, t in logs:
            freq[i].add(t)
        
        count = defaultdict(int)
        for key in freq:
            count[key] = len(freq[key])

            
        ans = [0] * k
        for key in count:
            ans[count[key] - 1] += 1
        return ans