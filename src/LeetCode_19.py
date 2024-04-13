# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # counting from the head
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        idx = size - n
        prev = None
        cur = head
        for i in range(idx):
            prev = cur
            cur = cur.next
        if prev:
            prev.next = cur.next
        elif head:
            head = head.next
        else:
            head = None
            
        return head