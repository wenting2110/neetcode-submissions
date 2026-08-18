# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = head
        length = 0
        while s != None:
            length += 1
            s = s.next
        
        idx = length - n
        s = head
        if idx == 0:
            return head.next
        for i in range(idx-1):
            s = s.next
        s.next = s.next.next

        return head