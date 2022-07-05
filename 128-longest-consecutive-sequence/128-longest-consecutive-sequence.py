class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = Counter(nums)
        
        count = 0
        for i in lst.keys():
            if not lst.get(i-1):
                num = i
                length = 0
                while num in lst:
                    length += 1
                    num += 1
                    
                count = max(count, length)
        
        return count