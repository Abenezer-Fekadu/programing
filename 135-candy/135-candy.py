class Solution:
    def candy(self, ratings: List[int]) -> int:
        lst = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1] and lst[i] <= lst[i-1]:
                lst[i] = lst[i-1] + 1
                
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1] and lst[j] <= lst[j+1]:
                lst[j] = lst[j+1] + 1
                
        return sum(lst)