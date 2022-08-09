class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
            
        arr.sort()
        for i in range(1, len(arr)):
            for j in range(i):
                quotient = arr[i] // arr[j]
                if quotient < 2 or math.sqrt(arr[i]) > arr[i- 1]:
                    break
                if arr[i] % arr[j] == 0:
                    count[arr[i]] += count[arr[j]] * count.get(quotient, 0)
                    count[arr[i]] %= mod
                  
        ans  = sum(count.values())
        return ans % mod