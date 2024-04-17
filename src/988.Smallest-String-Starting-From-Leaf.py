# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest_str = 'z' * 8501

        def traverse(node, path) -> None:
            nonlocal smallest_str

            if not node:
                return

            path.append(chr(node.val + 97))
            if not node.left and not node.right:
                curr = ''.join(path[::-1])
                smallest_str = min(smallest_str, curr)
                path.pop()

                return

            traverse(node.left, path)
            traverse(node.right, path)
            path.pop()

            return
        
        traverse(root, [])
        return smallest_str
