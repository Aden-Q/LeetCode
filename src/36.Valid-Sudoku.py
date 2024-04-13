class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in range(9):
            counter = Counter()
            for col in range(9):
                if board[row][col] == '.':
                    # not filled, skip
                    continue
                counter[board[row][col]] += 1
                if counter[board[row][col]] > 1:
                    # found duplicate, invalid
                    return False

        # check column
        for col in range(9):
            counter = Counter()
            for row in range(9):
                if board[row][col] == '.':
                    # not filled, skip
                    continue
                counter[board[row][col]] += 1
                if counter[board[row][col]] > 1:
                    # found duplicate, invalid
                    return False

        # check 3x3 grid
        for row_idx in range(3):
            for col_idx in range(3):
                counter = Counter()
                for row_offset in range(3):
                    for col_offset in range(3):
                        row = row_idx * 3 + row_offset
                        col = col_idx * 3 + col_offset
                        if board[row][col] == '.':
                            # not filled, skip
                            continue
                        counter[board[row][col]] += 1
                        if counter[board[row][col]] > 1:
                            # found duplicate, invalid
                            return False

        return True