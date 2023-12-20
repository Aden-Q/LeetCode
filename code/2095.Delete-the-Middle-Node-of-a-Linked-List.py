# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # an edge case when the previous node of the middle node is None
        if not head.next:
            return None

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # slow is the ascedence of the middle node
        slow.next = slow.next.next
        return head
