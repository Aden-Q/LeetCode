class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.is_bipartite = True
        visited = [False] * (n + 1)
        color = [False] * (n + 1)
        # build a graph
        graph = [[] for _ in range(n + 1)]
        for edge in dislikes:
            # undirected graph
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            nonlocal graph, color, visited
            visited[node] = True
            for next_node in graph[node]:
                if not visited[next_node]:
                    color[next_node] = not color[node]
                    dfs(next_node)
                elif color[next_node] == color[node]:
                    # is not bipartite
                    self.is_bipartite = False
                    return            
            
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i)
                if not self.is_bipartite:
                    return False
        return True