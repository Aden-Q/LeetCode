# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        # this function test whether a given hash dict can be rearrange to be palindrom or not
        def canBePalindromic(counter) -> bool:
            count_odd = 0
            for val in counter.values():
                if val % 2 == 1:
                    count_odd += 1
            
            return count_odd < 2
        
        res = 0
        def backtrack(node, path) -> None:
            nonlocal res
            if not node:
                return

            path[node.val] += 1
            if (not node.left) and (not node.right) and canBePalindromic(path):
                res += 1
            
            backtrack(node.left, path)
            backtrack(node.right, path)
            path[node.val] -= 1
            if path[node.val] == 0:
                del path[node.val]

            return

        backtrack(root, Counter())
        return res
