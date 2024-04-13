# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = head
        next_node = p.next
        while next_node:
            while next_node and p.val == next_node.val:
                next_node = next_node.next
            p.next = next_node
            p = next_node
            if p:
                next_node = p.next
        return head