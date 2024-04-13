# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_head = list2
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next

        a_prev = list1
        for _ in range(a-1):
            a_prev = a_prev.next
        
        b_next = a_prev
        for _ in range(b-a+2):
            b_next = b_next.next
        
        a_prev.next = list2_head
        list2_tail.next = b_next

        return list1
