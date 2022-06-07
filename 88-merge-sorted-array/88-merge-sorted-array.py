class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = 0 
        for i in range(m, m+n):
            nums1[i] = nums2[l] 
            l +=1 
        return nums1.sort()
            
        