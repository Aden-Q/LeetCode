# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # by m >= 1, we will keep at least 1 node, so we can safely return the original head
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            for _ in range(m):
                if not curr:
                    break
                curr = curr.next
            
            # now the first node to delete is curr.next
            for _ in range(n):
                if not curr or not curr.next:
                    break
                curr.next = curr.next.next

        return dummy.next
