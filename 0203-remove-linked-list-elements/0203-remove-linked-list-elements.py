# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = ListNode(0, head)
        
        node = root
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            
            if node.next and node.next.val != val:
                node = node.next
        
        return root.next
                