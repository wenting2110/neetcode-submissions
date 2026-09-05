# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        pos = 1
        num_1 = 0
        while l1:
            num_1 += l1.val * pos
            pos *= 10
            l1 = l1.next
        
        cur = l2
        pos = 1
        num_2 = 0
        while cur:
            num_2 += cur.val * pos
            pos *= 10
            cur = cur.next
        
        num = num_1 + num_2
        print(num_1)

        l3 = [int(x) for x in str(num)]
        head = ListNode(l3[-1])
        cur = head
        for i in range(len(l3)-1):
            cur.next = ListNode(val = l3[-i - 2])
            cur = cur.next

        return head