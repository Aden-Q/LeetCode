# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Global var counting the maximum length so far during traversal
        maxVal = 1
        # This function returns the length of the longest increasing sequence
        # and the lenght of the longest decreasing sequence starting from the root node
        # as a tuple
        # Should run postorder because we need to solve the subproblems (left tree and right tree) first
        def longestPath(root):
            nonlocal maxVal
            if not root:
                return 0, 0
            
            # Initial value for a single node tree
            icr, dcr = 1, 1
            # Update the length for the current root
            if root.left:
                left_icr, left_dcr = longestPath(root.left)
                if root.val == root.left.val - 1:
                    icr = left_icr + icr
                elif root.val == root.left.val + 1:
                    dcr = left_dcr + dcr
            if root.right:
                right_icr, right_dcr = longestPath(root.right)
                if root.val == root.right.val - 1:
                    icr = max(icr, right_icr + 1)
                elif root.val == root.right.val + 1:
                    dcr = max(dcr, right_dcr + 1)
            
            # Update the global var, chain icr and dcr together, the root node is count twice so reduce by 1
            maxVal = max(maxVal, icr + dcr - 1)
            return icr, dcr
        
        longestPath(root)
        # O(N) time and space solution (recursion depth N)
        return maxVal