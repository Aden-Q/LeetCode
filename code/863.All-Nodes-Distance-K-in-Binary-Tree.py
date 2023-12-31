# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def addParent(node: TreeNode):
            if not node:
                return node

            if node.left:
                node.left.parent = node

            if node.right:
                node.right.parent = node

            addParent(node.left)
            addParent(node.right)

            return
        
        root.parent = None
        addParent(root)

        ans = []
        visited = set()
        # run dfs starting from some node, the distance is the distance to the initial node (target in our case)
        def dfs(node, dist: int) -> None:
            nonlocal ans, visited
            if not node or node in visited:
                return
            
            visited.add(node)
            if dist == k:
                ans.append(node.val)
                # no need to explore further
                return

            dfs(node.parent, dist+1)
            dfs(node.left, dist+1)
            dfs(node.right, dist+1)

            return

        dfs(target, 0)
        return ans
