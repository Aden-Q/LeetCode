class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)
        graph = [[] for _ in range(n)]
        in_degrees = [0] * n

        def buildGraph(graph):
            for node in range(1, n):
                graph[parent[node]].append(node)
                graph[node].append(parent[node])
                in_degrees[parent[node]] += 1

            return

        buildGraph(graph)
        # keep track of the maximum path length from a leaf node to this node
        max_paths_len = [1] * n
        # a global var to keep track of the longest path length
        max_path_len = 1
        queue = deque()

        # collect all leaf nodes
        for i in range(n):
            if in_degrees[i] == 0:
                queue.append(i)

        # run topological sort from all leaf nodes
        # we can always traverse the whole graph, because it's a tree
        while queue:
            curr_node = queue.popleft()
            for next_node in graph[curr_node]:
                if in_degrees[next_node] == 0:
                    # a visited array, don't visit the same node twice in the topological sort
                    continue 

                if s[curr_node] != s[next_node]:
                    # we can connect the current path to it
                    max_path_len = max(max_path_len, max_paths_len[next_node] + max_paths_len[curr_node])
                    max_paths_len[next_node] = max(max_paths_len[next_node], max_paths_len[curr_node] + 1)
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    queue.append(next_node)
        
        return max_path_len
