class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         check dictionary
        check = defaultdict(int)
        
#         Itrate over the the numbers and check the duplicate in the dictionary
        for i in range(len(nums)):
            if nums[i] in check:
                if abs(i - check[nums[i]]) <= k:
                    return True
                
#                 add in the dictionary
            check[nums[i]] = i
            
        return False
                
    
