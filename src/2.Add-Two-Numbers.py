# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def addNodeWithCarry(node1, node2, carry) -> ListNode:
            if not node1 and not node2:
                if carry:
                    return ListNode(carry)
                else:
                    return None
            if not node1:
                curr = ListNode((node2.val + carry) % 10)
                carry = 1 if node2.val + carry >= 10 else 0
                curr.next = addNodeWithCarry(None, node2.next, carry)
            elif not node2:
                curr = ListNode((node1.val + carry) % 10)
                carry = 1 if node1.val + carry >= 10 else 0
                curr.next = addNodeWithCarry(node1.next, None, carry)
            else:
                curr = ListNode((node1.val + node2.val + carry) % 10)
                carry = 1 if node1.val + node2.val + carry >= 10 else 0
                curr.next = addNodeWithCarry(node1.next, node2.next, carry)

            return curr

        return addNodeWithCarry(l1, l2, 0)