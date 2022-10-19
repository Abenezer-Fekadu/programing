# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:    
        if not head:
            return head
        
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        
        k = k%size
        if k == 0:
            return head
        
        fast  = head
        for i in range(k):
            fast = fast.next
            
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        node = TreeNode(0)
        node.next = slow.next
        fast.next = head
        slow.next = None

        return node.next