class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        num = ''
        for n in nums:
            num += str(n)
            
        num = str(int(''.join(num)) + k)
        
        ans = []
        for n in num:
            ans.append(int(n))
        
        return ans
        
         