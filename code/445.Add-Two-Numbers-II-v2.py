# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head):
            prev = None
            curr = head
            
            while curr:
                next_temp = curr.next
                # 1 (prev) -> 2 (curr) -> 3 (next)
                curr.next = prev
                prev = curr
                curr = next_temp
            
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        head = None
        # Carry bit
        carry = 0
        
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            currSum = l1Val + l2Val + carry
            newNode = ListNode(currSum % 10)
            carry = currSum // 10
            newNode.next = head
            head = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head