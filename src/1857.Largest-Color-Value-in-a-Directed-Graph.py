class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # DFS
        INF = float("inf")
        n = len(colors)
        m = len(edges)
        color_count = [26 * [0] for _ in range(n)]
        graph = defaultdict(list)

        # build the graph
        for first, second in edges:
            graph[first].append(second)

        visited = [0] * n

        def dfs(node):
            nonlocal visited, INF, color_count
            if visited[node] == 1:
                # loop detected
                return INF
            if visited[node] == 2:
                return color_count[node][ord(colors[node]) - ord("a")]

            visited[node] = 1
            for next_node in graph[node]:
                res = dfs(next_node)
                if res == INF:
                    return INF
                for c in range(26):
                    color_count[node][c] = max(
                        color_count[node][c], color_count[next_node][c]
                    )

            color = ord(colors[node]) - ord("a")
            color_count[node][color] += 1
            visited[node] = 2

            return color_count[node][color]

        ans = 0
        for node in range(n):
            max_count = dfs(node)
            if max_count == INF:
                # loop
                return -1
            ans = max(ans, max_count)

        return ans
