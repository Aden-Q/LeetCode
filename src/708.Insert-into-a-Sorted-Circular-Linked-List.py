"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        prev, curr = head, head.next
        while True:
            if curr.val >= insertVal >= prev.val:
                # we've found an insert position
                prev.next = Node(insertVal, curr)
                return head
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    # we can insert
                    prev.next = Node(insertVal, curr)
                    return head
            
            # otherwise we need to go around
            prev, curr = curr, curr.next
            
            if prev == head:
                break

        # we break out of the loop
        prev.next = Node(insertVal, curr)
        return head
