# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)

        def traverse(node, parent):
            nonlocal adj
            if not node:
                return

            if parent:
                adj[node.val].append(parent.val)

            if node.left:
                adj[node.val].append(node.left.val)
            
            if node.right:
                adj[node.val].append(node.right.val)

            traverse(node.left, node)
            traverse(node.right, node)

            return

        traverse(root, None)

        q = deque([start])
        step = 0
        visited = set([start])
        while q:
            size = len(q)
            step += 1
            for _ in range(size):
                curr_node = q.popleft()
                for next_node in adj[curr_node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        q.append(next_node)

        return step - 1
