# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(head):
            nonlocal k
            curr = head
            for _ in range(k):
                if not curr:
                    # when the number of nodes remaining is not sufficient, do not do anything
                    return head
                curr = curr.next

            # reverse the first k nodes starting from head
            prev, curr = None, head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node

            # recursively reverse the remaining
            next_head = reverseK(curr)
            head.next = next_head
            return prev

        return reverseK(head)
