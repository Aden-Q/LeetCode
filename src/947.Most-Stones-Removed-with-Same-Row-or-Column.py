class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        # graph as an adjacency list
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                stone_A, stone_B = stones[i], stones[j]
                if stone_A[0] == stone_B[0] or stone_A[1] == stone_B[1]:
                    # share the same row or column
                    adj[i].append(j)
                    adj[j].append(i)

        visited = [False] * n
        # to count the number of connected components
        cnt = 0

        def dfs(idx) -> None:
            nonlocal visited
            if visited[idx]:
                return

            # visit every node only once
            visited[idx] = True

            for next_node in adj[idx]:
                dfs(next_node)

            return

        for i in range(n):
            if visited[i]:
                continue
            cnt += 1
            dfs(i)

        return n - cnt
