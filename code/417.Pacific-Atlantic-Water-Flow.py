class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited_po = [[False] * n for _ in range(m)]
        visited_ao = [[False] * n for _ in range(m)]
        res = []
        
        def dfs_po(x, y):
            nonlocal m, n, heights, dirs, visited_po
            if visited_po[x][y]:
                return
            visited_po[x][y] = True
            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >=n or heights[new_x][new_y] < heights[x][y]:
                    continue
                dfs_po(new_x, new_y)
            return
            
        def dfs_ao(x, y):
            nonlocal m, n, heights, dirs, visited_ao
            if visited_ao[x][y]:
                return
            visited_ao[x][y] = True
            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >=n or heights[new_x][new_y] < heights[x][y]:
                    continue
                dfs_ao(new_x, new_y)
            return
            
        for i in range(m):
            dfs_po(i, 0)
        for j in range(n):
            dfs_po(0, j)
        
        for i in range(m):
            dfs_ao(i, n-1)
        for j in range(n):
            dfs_ao(m-1, j)
            
        for i in range(m):
            for j in range(n):
                if visited_ao[i][j] and visited_po[i][j]:
                    res.append([i, j])
            
        return res