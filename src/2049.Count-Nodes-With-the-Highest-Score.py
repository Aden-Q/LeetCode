class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # total size: n, for each node, if it has a parent, then num_components += 1
        # if it has a left child, then num_components += 1, if it has a right child, then  num_components += 1
        n = len(parents)
        tree = {}
        for i in range(n):
            tree[i] = TreeNode(i)

        for i in range(1, n):
            parent = tree[parents [i]]
            curr = tree[i]
            if not parent.left:
                parent.left = curr
            else:
                parent.right = curr
        
        max_prod = 0
        cnt = 0
        # postordedr traversal, returns the subtree size rooted at node
        def dfs(node) -> int:
            nonlocal tree, n, max_prod, cnt
            if not node:
                return 0

            curr_prod = 1
            left_count = right_count = 0
            if node.left:
                left_count = dfs(node.left)
                curr_prod *= left_count
            if node.right:
                right_count = dfs(node.right)
                curr_prod *= right_count
            if node.val != 0:
                curr_prod *= (n - right_count - left_count - 1)
            
            if curr_prod > max_prod:
                max_prod = curr_prod
                cnt = 1
            elif curr_prod == max_prod:
                cnt += 1

            return right_count + left_count + 1

        root = tree[0]
        dfs(root)
        return cnt
