# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_list = []
        
        def traverse(head):
            nonlocal node_list
            if not head:
                return
            node_list.append(head.val)
            traverse(head.next)
            return
        
        traverse(head)
        max_val = 0
        for i in range(len(node_list) // 2):
            cur_val = node_list[i] + node_list[-1-i]
            max_val = max(max_val, cur_val)
        
        return max_val 