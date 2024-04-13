# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        has_parent = defaultdict(bool)
        tree_nodes = {}

        for parent, child, isLeft in descriptions:
            has_parent[child] = True
            if child not in tree_nodes:
                tree_nodes[child] = TreeNode(child)
            if parent not in tree_nodes:
                tree_nodes[parent] = TreeNode(parent)
            
            if isLeft:
                tree_nodes[parent].left = tree_nodes[child]
            else:
                tree_nodes[parent].right = tree_nodes[child]

        for val, node in tree_nodes.items():
            if not has_parent[val]:
                return node
