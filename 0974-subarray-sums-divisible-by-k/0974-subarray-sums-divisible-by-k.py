class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        
        ans, pref = 0, 0
        for num in nums:
            pref += num
            carry = pref % k
            
            if count.get(carry):
                ans += count.get(carry)
            else:
                count[carry] = 0
            
            count[carry] += 1
        return ans