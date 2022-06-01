# 1290. Convert Binary Number in a Linked List to Integer
**Difficulty:** Easy

## URL

https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

## Solution

### Approach 1:

The code is shown below:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        self.val = []
        
        def traverse(head) -> None:
            if not head:
                return
            self.val.append(str(head.val))
            traverse(head.next)
            return
        
        traverse(head)
        return int(''.join(self.val), 2)
```

