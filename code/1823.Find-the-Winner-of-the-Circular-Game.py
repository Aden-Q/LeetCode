class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # This is can solve by a circular linked list, we linked
        # those friends in clockwise order and tail to head to form a circle
        # Considering that we have n friends initially and we need to get rid of n - 1 of them
        # We need to perform n - 1 rounds traversal && deletion
        # And leave only one node in the linked list finally, forming a self loop
        if n == 1:
            return 1
        
        head = ListNode(val = 1)
        curr = head
        for val in range(2, n + 1):
            newNode = ListNode(val)
            curr.next = newNode
            curr = newNode
        # In the end linked the tail and head
        curr.next = head
        prev = curr
        curr = head
        
        # n - 1 rounds deletion
        for _ in range(n - 1):
            for _ in range(k-1):
                prev = curr
                curr = curr.next
            # We need to delete the curr node
            # prev -> curr -> next
            prev.next = curr.next
            curr = curr.next
        
        return curr.val