# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class heapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge 2 linkedlist list in sorted order and return the head
        def merge(head1, head2) -> Optional[ListNode]:
            dummy_head = ListNode()
            tail = dummy_head
            ptr1, ptr2 = head1, head2
            while ptr1 and ptr2:
                if ptr1.val > ptr2.val:
                    tail.next = ptr2
                    ptr2 = ptr2.next
                else:
                    tail.next = ptr1
                    ptr1 = ptr1.next
                tail = tail.next
            
            if ptr1:
                tail.next = ptr1
            else:
                tail.next = ptr2

            return dummy_head.next
            
        # split a linkedlist into 2 equal-size linked lists and return the head of the split point
        def getMid(head):
            if not head or not head.next:
                return head

            slow, fast = None, head
            while fast and fast.next:
                slow = head if not slow else slow.next
                fast = fast.next.next
            
            res = slow.next
            slow.next = None
            return res

        if not head or not head.next:
            return head
        # merge sort, divide and conquer
        mid = getMid(head)
        # merge sort the first half
        first = self.sortList(head)
        # merge sort the second half
        second = self.sortList(mid)
        return merge(first, second)