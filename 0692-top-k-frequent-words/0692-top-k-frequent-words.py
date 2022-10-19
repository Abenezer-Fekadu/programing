class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        ans = sorted(count, key=lambda c: (-count[c], c))
        return ans[:k]
 
