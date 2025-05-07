class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # total number of paris: n*(n-1)/2
        # number of connected pairs. within a connected component of k nodes:
        # k*(k-1)/2
        # so we can do dfs to iterate the graph and do substractions to get the final answer
        m = len(edges)
        # first we need to build the graph, as an adjacancy list
        graph = [[] for _ in range(n)]

        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        visited = [False] * n

        # recursively visit nodes and return the number of nodes in the connected component
        def dfs(i) -> int:
            nonlocal visited
            if visited[i]:
                return 0

            visited[i] = True
            total = 0
            for next_node in graph[i]:
                total += dfs(next_node)

            return total + 1

        ans = n * (n - 1) // 2
        for i in range(n):
            if visited[i]:
                continue
            k = dfs(i)
            ans -= k * (k - 1) // 2

        return ans
