# Space Optimized - I: space O(1) 背
# copy the list without using extra space like a hash map
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        l1 = head
        while l1:
            '''
            A → A' → B → B' → C → C'
            '''
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
        
        newHead = head.next

        l1 = head
        while l1:
            '''
            Set random of the copied node:
            A'.random = A.random.next
            '''
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        
        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next # A → B
            if l2.next:
                l2.next = l2.next.next # A' → B'
            l1 = l1.next
        
        return newHead
