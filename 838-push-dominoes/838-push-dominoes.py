class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lst = list('L' + dominoes + 'R')
        l, r = 0, 1
        while r < len(lst):
            if lst[r] == '.':
                r += 1
                continue
            elif lst[r] == 'L' and lst[l] == 'R':
                h = (r - l - 1) // 2
                lst[l+1:l+1+h] = ['R'] * h
                lst[r-h:r] = ['L'] * h
                
            elif lst[l] == lst[r]:
                lst[l+1:r] = [lst[l]] * (r - l - 1)
                
            l, r = r, r + 1
        return ''.join(lst[1:-1])    