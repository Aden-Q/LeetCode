# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sl = deque()
        gl = deque()
        l = deque()
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        for i in l:
            if i < x:
                sl.append(i)
            else:
                gl.append(i)
        cur = head
        while cur:
            while sl:
                cur.val = sl.popleft()
                cur = cur.next
            while gl:
                cur.val = gl.popleft()
                cur = cur.next
        return head