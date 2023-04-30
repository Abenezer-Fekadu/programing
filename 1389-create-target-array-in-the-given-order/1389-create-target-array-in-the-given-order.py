class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for num, i in zip(nums, index): 
            arr[i:i] = [num]
        return arr