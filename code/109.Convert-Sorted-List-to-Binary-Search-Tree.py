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
        # One pass to convert a linked list to an array
        # O(n)
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        # build BST using the sorted array
        
        def buildBST(left, right):
            nonlocal nums
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(val = nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root
              
        return buildBST(0, len(nums) - 1)