# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # mono strickly decreasing stack
        stack = []
        node = head
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()

            stack.append(node)

            node = node.next

        if not stack:
            return None

        newHead = stack[0]
        cur = newHead

        for i in range(1, len(stack)):
            cur.next = stack[i]
            cur = stack[i]

        cur.next = None
        return newHead
