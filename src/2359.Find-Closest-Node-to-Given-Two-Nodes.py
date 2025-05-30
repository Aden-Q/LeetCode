class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # from the problem description, there's at most 1 outgoing edge from a node
        # also we want  to terminate if we encounter a loop
        # 1. We do dfs starting from node1, save the distance on the path
        # 2. We do dfs starting from node2, save the distance on the path
        # 3. Calculate the global minimum distance on the visiting path
        n = len(edges)

        def dfs(node, curr_dist, visited, dist_from_node):
            if node == -1:
                return

            if visited[node]:
                return

            visited[node] = True
            dist_from_node[node] = curr_dist

            dfs(edges[node], curr_dist + 1, visited, dist_from_node)

            return

        dist_from_node1 = [-1] * n
        dist_from_node2 = [-1] * n

        dfs(node1, 0, [False] * n, dist_from_node1)
        dfs(node2, 0, [False] * n, dist_from_node2)

        min_max = float("inf")
        optimal_node = -1
        for i in range(n):
            if dist_from_node1[i] == -1 or dist_from_node2[i] == -1:
                continue
            if max(dist_from_node1[i], dist_from_node2[i]) < min_max:
                min_max = max(dist_from_node1[i], dist_from_node2[i])
                optimal_node = i

        return optimal_node
