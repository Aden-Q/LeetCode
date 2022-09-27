# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # This is an O(N) time and O(N) space solution, where N is the maximum length of the linked list
        # Because we need to add from the tail to front
        # Stack can do this for us
        # We can traverse both lists, append elements into two different stacks
        # Then we retrieve elements from stacks, add them up and construct a resulting list
        head = None
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        # Retrieve vals from both stacks and construct the list
        carry = 0  # this is the carry bit
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            currSum = val1 + val2 + carry
            newNode = ListNode(currSum % 10)
            carry = currSum // 10
            # We add the new node to the head of the linkedlist
            newNode.next = head
            # New head
            head = newNode
        
        return head