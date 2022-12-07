class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        color = [False] * len(graph)
        is_bipartite = True
        
        def traverse(node):
            nonlocal is_bipartite, color, visited
            if not is_bipartite:
                return
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    color[neighbour] = not color[node]
                    traverse(neighbour)
                else:
                    # check color consistency
                    if color[neighbour] == color[node]:
                        is_bipartite = False
                        return
            
        for node in range(len(graph)):
            traverse(node)
            
        return is_bipartite