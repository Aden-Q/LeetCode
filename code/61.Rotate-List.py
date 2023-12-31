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
        node = head
        while node:
            size += 1
            node = node.next

        k = k % size
        if k == 0:
            return head

        fast = head
        for _ in range(k):
            fast = fast.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
