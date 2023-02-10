class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        one = []
        for i in range(n**2):
            if img1[i//n][i%n]:
                one.append((i%n, i//n))
        two = []
        for j in range(n**2):
            if img2[j//n][j%n]:
                two.append((j%n, j//n))
    
        nums = []
        for i, j in one:
            for l, k in two:
                nums.append((i-l, j-k))
        
        count = Counter(nums)
        return max(count.values()) if count else 0