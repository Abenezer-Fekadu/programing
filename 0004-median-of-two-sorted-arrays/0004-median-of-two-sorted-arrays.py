class Solution:
    def findMedianSortedArrays(self, nums1, nums2): 
        ans = [] 
        l, r = 0, 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                ans.append(nums1[l])
                l += 1
            else:
                ans.append(nums2[r])
                r += 1
            
        ans += nums1[l:] + nums2[r:]
        if len(ans) % 2 != 0:
            return ans[len(ans)//2]
        
        return (ans[len(ans)//2 - 1] + ans[len(ans)//2]) / 2 
