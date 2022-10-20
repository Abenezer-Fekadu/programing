class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        ans = []
        for i in range(1, n+1):
            if i not in count:
                ans.append(i)
                
        return ans