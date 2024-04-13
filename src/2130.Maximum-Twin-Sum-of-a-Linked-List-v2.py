# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # we reverse the first half of the linkedlist
        # on the go, we should have access to both headers of the lists
        prev = None
        curr = head
        fast = head
        while fast:
            fast = fast.next.next
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        head1 = prev
        head2 = curr
        max_sum = 0
        while head1:
            max_sum = max(max_sum, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
        
        return max_sum
