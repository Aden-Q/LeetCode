class TreeNode:
    def __init__(self, val=None, weight=None, children=None):
        self.val = val
        # its weight to its parent
        self.weight = weight
        # a map from a TreeNode to the edge weight
        self.children = children if children else []

class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        # we cannot use greedy because of example 1
        tree_nodes = {}

        for i in range(len(edges)):
            tree_nodes[i] = TreeNode(i, 0)

        for i in range(1, len(edges)):
            parent, weight = edges[i][0], edges[i][1]
            child = tree_nodes[i]
            child.weight = weight
            tree_nodes[parent].children.append(child)

        @cache
        def dp(node, parent_edge_chosen: bool) -> int:
            if not node.children:
                return 0

            child_scores_with_unchosen = [dp(child, False) for child in node.children]
            all_scores = sum(child_scores_with_unchosen)
            max_score = max(0, all_scores)
            if parent_edge_chosen:
                return max_score

            # the parent edge is not chosen, we can freely choose at most one of the edge
            child_scores_with_chosen = [(dp(child, True), child.weight) for child in node.children]

            for i in range(len(node.children)):
                max_score = max(max_score, all_scores - child_scores_with_unchosen[i] + child_scores_with_chosen[i][0] + child_scores_with_chosen[i][1])

            return max_score

        return dp(tree_nodes[0], False)
