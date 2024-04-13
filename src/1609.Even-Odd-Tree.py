# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # level order traversal

        isEven = True

        q = deque([root])
        while q:
            size = len(q)
            prev_val = float('inf')
            if isEven:
                prev_val = -prev_val

            for _ in range(size):
                curr_node = q.popleft()
                if isEven:
                    if curr_node.val % 2 == 0:
                        return False
                    if curr_node.val <= prev_val:
                        return False
                else:
                    if curr_node.val % 2 == 1:
                        return False
                    if curr_node.val >= prev_val:
                        return False

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                prev_val = curr_node.val
            
            # flip the flag
            isEven = not isEven

        return True
