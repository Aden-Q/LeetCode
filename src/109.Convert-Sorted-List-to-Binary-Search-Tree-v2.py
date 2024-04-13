# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        cur = head
        
        def traverse(left, right):
            nonlocal cur
            if left > right:
                return None
            mid = (left + right) // 2
            leftTree = traverse(left, mid - 1)
            node = TreeNode(val = cur.val)
            cur = cur.next
            rightTree = traverse(mid + 1, right)
            node.left = leftTree
            node.right = rightTree
            return node
        
        return traverse(0, length - 1)