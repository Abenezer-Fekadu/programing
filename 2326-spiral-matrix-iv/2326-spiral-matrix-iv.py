# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # direction array
        drt = [0, 1]
        ans = [[-1]*n for _ in range(m)]
        
        # check if in bound
        bound = lambda row, col: 0 <= row < m and 0 <= col < n
        
        # populate the our answer array
        row, col = 0, 0
        while head:
            ans[row][col] = head.val
            if not bound(row+drt[0], col+drt[1]) or ans[row+drt[0]][col+drt[1]] != -1:
                drt[0], drt[1] = drt[1], -drt[0]
            
            row, col = row + drt[0], col + drt[1]
            head = head.next
            
        return ans
        