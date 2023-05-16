# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        
        if not temp or not temp.next: return head
            
        first = head
        second = head.next

        new = self.swapPairs(head.next.next)
        first.next = new
        second.next = first
        

        return second
        
            