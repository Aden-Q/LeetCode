class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        q = [(sr, sc)]
        # BFS
        while len(q) != 0:
            cur_x, cur_y = q.pop()
            if image[cur_x][cur_y] == oldColor:
                image[cur_x][cur_y] = newColor
                if cur_x - 1 >= 0:
                    q.append((cur_x - 1, cur_y))
                if cur_x + 1 < m:
                    q.append((cur_x + 1, cur_y))
                if cur_y - 1 >= 0:
                    q.append((cur_x, cur_y - 1))
                if cur_y + 1 < n:
                    q.append((cur_x, cur_y + 1))
    
        return image