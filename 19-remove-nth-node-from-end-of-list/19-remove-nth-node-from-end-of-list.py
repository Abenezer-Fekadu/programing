# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        
        count = 0
        while  count < n:
            r = r.next
            count += 1
                    
        if not r:
            return head.next
        
        while r and r.next:
            l = l.next
            r = r.next
                
        l.next = l.next.next
        
        return head
    