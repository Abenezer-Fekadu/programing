class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0
        for num in count.values():
            if num == 1:
                return -1
            
            ans += (num // 3)
            num = num % 3
            if num:
                ans += 1
            
        return ans