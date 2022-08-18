class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        res = 0      
        for num in count:
            if num + num == target:
                res += count[num] * (count[num]-1)
            elif num == target[:len(num)]:
                res += count[num] * count[target[len(num):]]
                
        return res