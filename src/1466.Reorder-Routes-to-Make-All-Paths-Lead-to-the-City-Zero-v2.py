class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        # build the graph as an adjacency list
        for source, dest in connections:
            # we need to tell from a real edge to a virtual edge
            graph[dest].append(source)
            graph[source].append(-dest)

        visited = [False] * n
        cnt = 0
        def dfs(curr) -> None:
            nonlocal cnt
            if visited[curr]:
                return
            visited[curr] = True

            # visit all its neighbors
            for neighbor in graph[curr]:
                if neighbor < 0 and not visited[-neighbor]:
                    # a virtual edge, we need to reverse it
                    cnt += 1
                dfs(abs(neighbor))

            return

        dfs(0)
        return cnt
