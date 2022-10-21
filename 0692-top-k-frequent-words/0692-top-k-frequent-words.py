class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict1, bucket, ans = Counter(words), [[] for _ in range(len(words)+1)], []
    
        for i in range(len(words)+1):
            bucket[i] = sorted([key for key, val in dict1.items() if dict1[key] == i])

        for i in range(len(words)-1,-1,-1):
            ans += bucket[i]

        return ans[:k]