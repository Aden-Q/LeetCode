# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        self.val = []
        
        def traverse(head) -> None:
            if not head:
                return
            self.val.append(str(head.val))
            traverse(head.next)
            return
        
        traverse(head)
        return int(''.join(self.val), 2)