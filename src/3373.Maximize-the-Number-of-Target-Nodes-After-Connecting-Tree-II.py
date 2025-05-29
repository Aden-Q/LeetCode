class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        # the idea is: for every node tree 1, the optimal node to connect to in tree 2 is always the same node
        # we can traverse the trees and mark nodes with 2 colors (0, 1), depending the number of nodes in between
        # the optimal node in tree2 is the node with the maximum number of nodes that are not target to this node
        # we can randomly choose a starting node and do traversal in a single pass for each tree
        # time complexity: O(n + m)
        # space complexity: O(n + m)
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        # build the graphs in adjacency list
        for first, second in edges1:
            graph1[first].append(second)
            graph1[second].append(first)

        for first, second in edges2:
            graph2[first].append(second)
            graph2[second].append(first)

        n, m = len(edges1) + 1, len(edges2) + 1

        # return a color graph
        def bfs(start, graph, num_nodes):
            visited = [False] * num_nodes
            colors = [0] * num_nodes

            q = deque([(start, 0)])

            while q:
                size = len(q)
                for _ in range(size):
                    curr_node, color = q.popleft()
                    visited[curr_node] = True
                    colors[curr_node] = color
                    next_color = 0 if color else 1

                    for next_node in graph[curr_node]:
                        if visited[next_node]:
                            continue
                        q.append((next_node, next_color))

            return colors

        colors1 = bfs(0, graph1, n)
        colors2 = bfs(0, graph2, m)

        count1_tree1 = sum(colors1)
        count0_tree1 = len(colors1) - count1_tree1

        ans = [count0_tree1 if colors1[idx] == 0 else count1_tree1 for idx in range(n)]

        count1_tree2 = sum(colors2)
        count0_tree2 = len(colors2) - count1_tree2

        max_val = max(count1_tree2, count0_tree2)

        ans = [val + max_val for val in ans]

        return ans
