"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        longest_path = 0

        # returns the height of the subtree starting at the current node
        def getHeight(node) -> int:
            # update this global var before returning when visiting some node
            nonlocal longest_path
            if not node:
                return 0

            max_height, second_max_height = -1, -1
            for child in node.children:
                height = getHeight(child)
                if height >= max_height:
                    max_height, second_max_height = height, max_height
                elif height > second_max_height:
                    second_max_height = height

            longest_path = max(longest_path, max_height + second_max_height + 2)

            return max_height + 1

        getHeight(root)
        return longest_path
