# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # two dummy heads
        small = ListNode()
        large = ListNode()
        small_cur = small
        large_cur = large
        cur = head
        while cur:
            if cur.val < x:
                small_cur.next = ListNode(cur.val)
                small_cur = small_cur.next
            else:
                large_cur.next = ListNode(cur.val)
                large_cur = large_cur.next
            cur = cur.next
        small_cur.next = large.next
        return small.next
                