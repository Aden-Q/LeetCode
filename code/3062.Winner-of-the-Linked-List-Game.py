# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        teamScoreDiff = 0

        node = head
        while node and node.next:
            if node.val > node.next.val:
                teamScoreDiff -= 1
            elif node.val < node.next.val:
                teamScoreDiff += 1

            node = node.next.next

        if teamScoreDiff > 0:
            return 'Odd'
        elif teamScoreDiff < 0:
            return 'Even'
        else:
            return 'Tie'
