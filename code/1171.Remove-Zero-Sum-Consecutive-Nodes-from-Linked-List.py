# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a 2-sum problem
        dummy = ListNode()
        dummy.next = head
        node_sum = {}
        node_sum[0] = dummy
        prefix_sum = 0

        node = head
        while node:
            prefix_sum += node.val
            if prefix_sum in node_sum:
                # yes this subsequence sums up to 0, we should delete nodes in between
                curr_node = node_sum[prefix_sum].next
                p_sum = curr_node.val + prefix_sum
                while p_sum != prefix_sum:
                    del node_sum[p_sum]
                    curr_node = curr_node.next
                    p_sum += curr_node.val
                
                node_sum[prefix_sum].next = node.next
            else:
                node_sum[prefix_sum] = node

            node = node.next

        return dummy.next
