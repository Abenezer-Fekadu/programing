# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        while node and node.next:
            if node.next == slow:
                node.next = slow.next
            
            node = node.next
            
        return dummy.next