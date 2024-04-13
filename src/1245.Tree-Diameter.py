class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        if n == 1:
            return 0

        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        def dfs(node, depth, visited):
            nonlocal max_depth, node_global

            visited[node] = True
            if depth > max_depth:
                node_global = node
                max_depth = depth
            
            for next_node in graph[node]:
                if visited[next_node]:
                    continue
                dfs(next_node, depth+1, visited)
            
            return

        node_global = None
        max_depth = 0
        dfs(0, 0, [False] * n)
        nodeA = node_global
        
        node_global = None
        max_depth = 0
        dfs(nodeA, 0, [False] * n)

        return max_depth
