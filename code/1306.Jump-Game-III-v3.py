class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        
        def dfs(pos):
            nonlocal visited, arr
            if pos >= len(arr) or pos < 0:
                return
            if visited[pos]:
                return
            visited[pos] = True
            for next_pos in [pos + arr[pos], pos - arr[pos]]:
                dfs(next_pos)
            return
        
        dfs(start)
        for idx, val in enumerate(arr):
            if val == 0 and visited[idx]:
                return True
        
        return False
            