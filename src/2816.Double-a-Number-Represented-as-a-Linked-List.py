# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # a helper function for tail recursion, returns the carry bit
        def helper(node) -> int:
            if not node:
                return 0

            carry = helper(node.next)
            newVal = node.val * 2 + carry
            node.val = newVal % 10

            return newVal // 10

        carry = helper(head)
        if carry:
            newHead = ListNode(carry, head)
            return newHead

        return head
