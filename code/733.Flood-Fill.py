class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        def dfs(r, c):
            nonlocal image, newColor, oldColor
            if image[r][c] == oldColor:
                image[r][c] = newColor
                if r - 1 >= 0:
                    dfs(r-1, c)
                if r + 1 < m:
                    dfs(r+1, c)
                if c - 1 >= 0:
                    dfs(r, c-1)
                if c + 1 < n:
                    dfs(r, c+1)
            
        dfs(sr, sc)
        return image