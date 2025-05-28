class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        # we should always connect to the same node in the second tree
        # to find the optimal node in the second tree, do BFS up to depth k - 1

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for first, second in edges1:
            graph1[first].append(second)
            graph1[second].append(first)

        for first, second in edges2:
            graph2[first].append(second)
            graph2[second].append(first)

        def bfs(start, graph, num_nodes, depth_limit):
            visited = [False] * num_nodes
            q = deque([start])

            depth = 0
            num_target = 0
            while q:
                if depth > depth_limit:
                    break
                size = len(q)
                num_target += size
                for _ in range(size):
                    node = q.popleft()
                    visited[node] = True

                    for next_node in graph[node]:
                        if not visited[next_node]:
                            q.append(next_node)

                depth += 1

            return num_target

        num_targets1 = [0] * (n)
        num_targets2 = [0] * (m)

        for i in range(n):
            num_targets1[i] = bfs(i, graph1, n, k)

        for i in range(m):
            num_targets2[i] = bfs(i, graph2, m, k - 1)

        max_node = max(num_targets2)

        return [val + max_node for val in num_targets1]
