class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        connect_arr = [[] for i in range(n)]
        for c in connections:
            connect_arr[c[0]].append(c[1])
            connect_arr[c[1]].append(c[0])
        visited = [False] * n
        path = []
        res = []
        def dfs(s):
            nonlocal visited, n, connect_arr, path
            if visited[s]:
                return
            visited[s] = True
            path.append(s)
            for next_pt in connect_arr[s]:
                dfs(next_pt)
            return
        
        cnt = 0
        redundant_cnt = 0
        for i in range(n):
            if not visited[i]:
                path = []
                cnt += 1
                dfs(i)
                num_edges = 0
                for node in path:
                    num_edges += len(connect_arr[node])
                num_edges = num_edges // 2
                redundant_cnt += num_edges - (len(path) - 1)
        
        if redundant_cnt >= cnt - 1:
            return cnt - 1
        else:
            return -1