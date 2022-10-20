class Solution:
    def intToRoman(self, num: int) -> str:
        nums = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        ans = ""
        while num > 0:
            for c in reversed(nums):
                if num >= c:
                    num -= c
                    ans += nums[c]
                    break
            
        return ans