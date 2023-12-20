class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build the graph as an adjacency list
        graph = [[] for _ in range(n)]
        visited = [False] * n

        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True
            for next_node in graph[node]:
                dfs(next_node)
            
            return

        cnt = 0
        for node in range(n):
            if visited[node]:
                continue
            dfs(node)
            cnt += 1
        
        return cnt