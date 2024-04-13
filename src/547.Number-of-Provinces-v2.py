from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def bfs(start):
            '''
            Args:
                start: source for running bfs
            '''
            nonlocal isConnected, n, visited
            q = deque([start])
            visited[start] = True
            while len(q) != 0:
                cur_node = q.popleft()
                for next_node in range(n):
                    if isConnected[cur_node][next_node] and not visited[next_node]:
                        visited[next_node] = True
                        q.append(next_node)
            return
                    
        ct = 0
        for i in range(n):
            if not visited[i]:
                ct += 1
                bfs(i)
        return ct