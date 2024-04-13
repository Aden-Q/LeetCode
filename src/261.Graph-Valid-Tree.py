from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False] * n
        q = deque()
        q.append(0)
        visited[0] = True
        num_visited = 1
        while len(q) != 0:
            sz = len(q)
            for _ in range(sz):
                cur_node = q.popleft()
                for next_node in graph[cur_node]:
                    if not visited[next_node]:
                        visited[next_node] = True
                        q.append(next_node)
                        num_visited += 1
        return num_visited == n