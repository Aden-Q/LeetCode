class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        color = [False] * len(graph)
        is_bipartite = True
        
        def bfs(node):
            nonlocal graph, visited, color, is_bipartite
            if not is_bipartite:
                return
            # visite the current node
            visited[node] = True
            q = [node]
            # run BFS
            while len(q) != 0:
                cur = q.pop()
                for neighbour in graph[cur]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        color[neighbour] = not color[cur]
                        q.append(neighbour)
                    elif color[neighbour] == color[cur]:
                        is_bipartite = False
                        return
            
        for node in range(len(graph)):
            if not visited[node]:
                bfs(node)
        return is_bipartite