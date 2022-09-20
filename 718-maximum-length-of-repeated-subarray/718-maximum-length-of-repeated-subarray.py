class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        num2 = ''.join([chr(i) for i in nums2])
        
        s = ""
        ans = 0
        for num in nums1:
            s += chr(num)
            if s in num2:
                ans = max(ans, len(s))
            else:
                s = s[1:]
        
        return ans