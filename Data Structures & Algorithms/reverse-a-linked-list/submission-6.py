# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # later = curr.next
            # curr.next = prev
            # prev = curr
            # curr = later
            
            # 右邊的值會先被計算成一個元組 (tuple)，再分配給左邊
            # 這樣就不需要手動寫暫存變數 next_node 了
            curr.next, curr, prev = prev, curr.next, curr
        
        return prev