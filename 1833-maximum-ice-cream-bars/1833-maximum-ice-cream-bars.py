class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for coin in costs:
            if coin <= coins:
                ans += 1
                coins -= coin
        return ans