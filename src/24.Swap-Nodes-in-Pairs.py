# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        prev_node = dummy_head
        # if any one of them is empty, we do not need to proceed
        while prev_node and prev_node.next and prev_node.next.next:
            curr_node = prev_node.next
            next_node = prev_node.next.next
            tmp_node = next_node.next
            prev_node.next = next_node
            next_node.next = curr_node
            curr_node.next = tmp_node

            prev_node = curr_node

        return dummy_head.next
