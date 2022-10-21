class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [0]*100001
        for num in nums: 
            bucket[num + 50000] += 1
                    
        ans = []
        for i, num in enumerate(bucket, -50000): 
            ans.extend([i]*num)
        return ans 