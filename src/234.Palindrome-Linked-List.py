# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        def traverse(head):
            nonlocal left
            if not head:
                return True
            res = traverse(head.next)
            res = res and left.val == head.val
            left = left.next
            return res
        return traverse(head)