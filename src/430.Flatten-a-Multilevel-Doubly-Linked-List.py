"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def recursiveFlatten(head):
            # This function is used to flatten a doubly linkied list
            # Then return the resulting list's tail node
            if not head:
                return head
            curr = head
            prev = None
            
            # Find a node whose child is not null
            while curr:
                next_node = curr.next
                if curr.child:
                    child_tail = recursiveFlatten(curr.child)
                    curr.next = curr.child
                    curr.child.prev = curr
                    child_tail.next = next_node
                    if next_node:
                        next_node.prev = child_tail
                    curr.child = None
                    prev = child_tail
                else:
                    prev = curr
                curr = next_node
            
            return prev
        
        recursiveFlatten(head)
        return head
    