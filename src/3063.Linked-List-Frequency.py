# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = Counter()
        node = head
        while node:
            counter[node.val] += 1
            node = node.next

        dummy = ListNode()
        node = dummy
        for val in counter.values():
            node.next = ListNode(val)
            node = node.next

        return dummy.next
