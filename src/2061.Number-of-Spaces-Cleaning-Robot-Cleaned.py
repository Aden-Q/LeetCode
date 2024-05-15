class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n = len(room), len(room[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        def isValid(row, col, idx) -> bool:
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            
            if room[row][col] == 1:
                return False

            return True

        cnt = 0
        def dfs(row, col, d_idx):
            nonlocal cnt, room, visited

            if (row, col, d_idx) in visited:
                return

            if room[row][col] == 0:
                cnt += 1
                room[row][col] = -1

            visited.add((row, col, d_idx))

            for offset in range(4):
                next_idx = (d_idx + offset) % 4
                d = directions[next_idx]
                next_row, next_col = row + d[0], col + d[1]
                if not isValid(next_row, next_col, next_idx):
                    continue

                dfs(next_row, next_col, next_idx)
                return

            return

        dfs(0, 0, 0)
        return cnt
