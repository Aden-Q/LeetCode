class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # We need to flatten the board into a 1D array to make it convenient.
        new_board = [-1]
        for row in range(n - 1, -1, -1):
            if (n - row) % 2 == 1:
                new_board.extend(board[row])
            else:
                new_board.extend(board[row][::-1])

        min_dist = [-1] * (n * n + 1)
        # starting at label 1
        min_dist[1] = 0
        q = deque([1])

        while q:
            curr_idx = q.popleft()
            # 6-side dice
            for offset in range(1, 7):
                next_idx = curr_idx + offset
                if next_idx > n * n:
                    continue
                # check whether we need to jump or not
                next_idx = (
                    next_idx if new_board[next_idx] == -1 else new_board[next_idx]
                )
                if next_idx == n * n:
                    return min_dist[curr_idx] + 1
                if min_dist[next_idx] == -1:
                    min_dist[next_idx] = min_dist[curr_idx] + 1
                    q.append(next_idx)

        return min_dist[n * n]
