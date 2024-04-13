# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # To simplify things a bit
        # We need to do two things:
        # 1. Reverse the second half of the linked list
        # 2. Combine the first half and the reversed second half alernatively
        if not head or not head.next or not head.next.next:
            return head

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # first, we need to reverse slow.next and set slow.next = None
        def reverseList(root) -> ListNode:
            if not root or not root.next:
                return root
            
            head = reverseList(root.next)
            root.next.next = root
            root.next = None
            return head

        first = head
        second = reverseList(slow.next)
        slow.next = None
        dummy = ListNode()
        curr = dummy

        # now we need to comine the first and the second lists
        while first or second:
            if first:
                curr.next = first
                curr = curr.next
                first = first.next
            if second:
                curr.next = second
                curr = curr.next
                second = second.next

        return dummy.next
