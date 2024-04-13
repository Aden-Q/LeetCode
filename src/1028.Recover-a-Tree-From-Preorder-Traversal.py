# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # a global index to traverse through the input array
        idx = 0
        val = 0
        depth = -1
        dummy = TreeNode()

        def parseInput():
            nonlocal idx, val, depth
            # only parse the input string when necessary
            if idx < len(traversal) and val == 0:
                # yes we need to parse the next node
                depth = 0
                while traversal[idx] == '-':
                    depth += 1
                    idx += 1

                val = 0
                while idx < len(traversal) and traversal[idx].isdigit():
                    val = val * 10 + int(traversal[idx])
                    idx += 1

        def dfs(parent, parent_depth) -> None:
            nonlocal idx, val, depth
            if not parent:
                return

            parseInput()

            # next we check whether we need to backtrack
            if parent_depth == depth - 1:
                if not parent.left:
                    parent.left = TreeNode(val)
                    val = 0
                    depth = -1
                    dfs(parent.left, parent_depth+1)

            if parent_depth == depth - 1:
                if not parent.right:
                    parent.right = TreeNode(val)
                    val = 0
                    depth = -1
                    dfs(parent.right, parent_depth+1)

            return

        dfs(dummy, -1)
        return dummy.left
