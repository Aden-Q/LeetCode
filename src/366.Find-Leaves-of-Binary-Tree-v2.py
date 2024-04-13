# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(N) time because we visit each node exactly once, calculating
        # its height and append it to the resulting list
        # O(N) space which mainly consists of res, every node is append to res in the end
        res = []
        
        def traverse(root):
            nonlocal res
            if not root:
                return 0
            left_height = traverse(root.left)
            right_height = traverse(root.right)
            cur_height = max(left_height, right_height) + 1
            if cur_height > len(res):
                res.append([root.val])
            else:
                res[cur_height-1].append(root.val)
            return cur_height
        
        traverse(root)
        return res