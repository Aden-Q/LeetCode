# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        
        def traverse(root):
            if not root:
                return -1
            cur_height = max(traverse(root.left), traverse(root.right)) + 1
            if cur_height + 1 > len(self.res):
                self.res.append([root.val])
            else:
                self.res[cur_height].append(root.val)
            return cur_height
        
        traverse(root)
        return self.res