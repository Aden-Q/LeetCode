class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])

        def dfs(row, col):
            nonlocal maze
            if maze[row][col] == 2:
                # this path has been discovered so we don't need to continue here
                return False

            if [row, col] == destination:
                return True

            maze[row][col] = 2
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_row, next_col = row + d[0], col + d[1]
                while 0 <= next_row < m and 0 <= next_col < n and maze[next_row][next_col] != 1:
                    # while we can go in this direction
                    next_row += d[0]
                    next_col += d[1]

                # revert the last movement and run dfs
                if dfs(next_row - d[0], next_col - d[1]):
                    # early return when the destination is discovered
                    return True

            return False

        return dfs(start[0], start[1])
