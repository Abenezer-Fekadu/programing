# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        val = head
        size = 0
        while val:
            size += 1
            val = val.next
        
        answer = 0
        stack = []
        temp = head
        i = 0
        while temp and i < size: 
            if i < (size//2):
                stack.append(temp.val)
            else:
                if stack != []:
                    num = stack.pop()
                    if (num + temp.val) > answer:
                        answer = num + temp.val
            i += 1
            temp = temp.next
            
        return answer