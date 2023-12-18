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
        if not head:
            return head
        heap = []

        node = head
        # iterate through the input linkedlist and push all into the minheap
        while node:
            heapq.heappush(heap, heapNode(node))
            node = node.next

        res = []
        while heap:
            res.append(heapq.heappop(heap))
        
        for i in range(len(res) - 1):
            res[i].node.next = res[i+1].node
        res[-1].node.next = None
        
        return res[0].node