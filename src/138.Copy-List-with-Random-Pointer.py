"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # A mapping from old nodes to new nodes
        ht = {}
        node = head
        while node:
            if node not in ht:
                ht[node] = Node(node.val)
            if node.next and node.next not in ht:
                ht[node.next] = Node(node.next.val)
            if node.random and node.random not in ht:
                ht[node.random] = Node(node.random.val)
            if node.next:
                ht[node].next = ht[node.next]
            if node.random:
                ht[node].random = ht[node.random]
            node = node.next
            
        return ht[head]