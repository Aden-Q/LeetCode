# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        maxCount = 0
        count = 0
        prev = None
        result = []
        
        def traversal(root):
            nonlocal maxCount, count, prev, result
            if not root:
                return
            
            traversal(root.left)
            if prev == None:
                count = 1
            elif prev.val == root.val:
                count += 1
            else:
                count = 1
            prev = root
            if count == maxCount:
                result.append(root.val)
            elif count > maxCount:
                maxCount = count
                result.clear()
                result.append(root.val)
            traversal(root.right)
        if not root:
            return []
        traversal(root)
        return result