# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()

        is_odd = True
        curr = head
        odd = odd_head
        even = even_head
        while curr:
            if is_odd:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            is_odd = not is_odd
            curr = curr.next
        
        even.next = None
        odd.next = even_head.next

        return odd_head.next