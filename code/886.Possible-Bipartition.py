class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [False] * (n + 1)
        color = [False] * (n + 1)
        is_bipartite = True
        graph = [[] for _ in range(n + 1)]
        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            nonlocal visited, color, is_bipartite, graph
            if not is_bipartite:
                return
            # visite the current node
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    color[neighbour] = not color[node]
                    dfs(neighbour)
                elif color[neighbour] == color[node]:
                    is_bipartite = False
                    return
            
        for node in range(1, n + 1):
            if not visited[node]:
                dfs(node)
                
        return is_bipartite