# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # add 1 to the list, using tail recursion, returns the carry bit
        def addOne(node: ListNode) -> int:
            if not node:
                return 1

            carry = addOne(node.next)
            if carry:
                node.val += 1
                if node.val == 10:
                    node.val = 0
                    # carry over
                    return carry
            
            return 0

        if addOne(head):
            # carry over from the head
            new_head = ListNode(1, head)
            return new_head

        return head
