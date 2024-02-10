class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

        visited = [False] * n
        # return whehter it's possible to reach from the current node to destination
        def dfs(node) -> bool:
            if node == destination:
                return True
            
            visited[node] = True
            for next_node in adj[node]:
                if visited[next_node]:
                    continue
                if dfs(next_node):
                    # if the next node can lead to destination, we don't need to explore further
                    return True
            
            return False

        return dfs(source)
