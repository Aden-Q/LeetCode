# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # reverse the first k nodes of the linkedlist
        def reverseLinkedList(head):
            prev, curr = None, head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev, curr = curr, next_node
            
            # link the tail to the next head
            head.next = curr

            return prev

        new_head = None
        ktail = None
        prev_head, curr_head = head, head
        while curr_head:
            for _ in range(k):
                if not curr_head:
                    return new_head if new_head else None
                curr_head = curr_head.next
            # now curr points to the next head

            # reverse the list starting at prev_head
            revHead = reverseLinkedList(prev_head)
            if not new_head:
                new_head = revHead
            
            if ktail:
                ktail.next = revHead
            
            # keep ktail as the previous point of curr_head (curr_head has not been reverted yet)
            ktail = prev_head
            prev_head = curr_head

        return new_head if new_head else head
