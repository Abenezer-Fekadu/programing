# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ans = set()
        while head and head.next:
            if head not in ans:
                ans.add(head)
            else:
                return True
            
            head = head.next
        return False