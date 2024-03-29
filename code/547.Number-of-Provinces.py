class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(s):
            nonlocal isConnected
            if visited[s]:
                return
            visited[s] = True
            for i in range(n):
                if isConnected[s][i]:
                    dfs(i)
                    
        ct = 0
        for i in range(n):
            if not visited[i]:
                ct += 1
                dfs(i)
        return ct