from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.is_bipartite = True
        visited = [False] * n
        # True and False represents two different colors
        color = [False] * n
        
        # the graph may not be connected
        # need to run dfs several times
        def dfs(node):
            nonlocal graph, color
            if not self.is_bipartite:
                return False
            visited[node] = True
            for next_node in graph[node]:
                if not visited[next_node]:
                    # assign a different color
                    color[next_node] = not color[node]
                    dfs(next_node)
                else:
                    if color[next_node] == color[node]:
                        # is not bipartite
                        self.is_bipartite = False
                        return
            
        for i in range(n):
            if not visited[i]:
                dfs(i)
                if not self.is_bipartite:
                    # early termination
                    return False
        return True