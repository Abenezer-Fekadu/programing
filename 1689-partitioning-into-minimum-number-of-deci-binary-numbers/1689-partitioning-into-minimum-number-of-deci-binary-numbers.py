class Solution:
    def minPartitions(self, n: str) -> int:
        for c in range(9, -1, -1):
	        if str(c) in n:
		        return c