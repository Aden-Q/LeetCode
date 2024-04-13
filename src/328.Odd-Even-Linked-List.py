# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # when the number of nodes is 0~2, no-op
        if not head or not head.next or not head.next.next:
            return head
        
        head_odd = head
        head_even = head.next

        curr_odd = head_odd
        tail_odd = head_odd
        curr_even = head_even
        while curr_odd and curr_odd.next:
            next_odd = curr_odd.next.next
            curr_odd.next = next_odd
            curr_odd = next_odd

            if curr_even.next:
                next_even = curr_even.next.next
                curr_even.next = next_even
                curr_even = next_even

            if curr_odd:
                tail_odd = curr_odd
        
        tail_odd.next = head_even

        return head_odd