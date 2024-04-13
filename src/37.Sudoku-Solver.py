class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9
        # all possible digits to fill into an empty slot
        digits = [str(digit) for digit in range(1, N+1)]
        # each row, col, box is a hashset, tracking the used numbers
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        # calculate the correct box index from (row, col)
        def calBoxIndex(row, col):
            return row // 3 * 3 + col // 3

        # check if a number can be filled into the slot board[row][col]
        def isValid(row, col, num):
            if board[row][col] != '.':
                return False
            if num in rows[row]:
                # the number has been used in the row
                return False
            if num in cols[col]:
                # the number has been used in the column
                return False
            if num in boxes[calBoxIndex(row, col)]:
                # the number has been used in the 3x3 box
                return False

            # it's a valid number if it passes all checks
            return True

        # dfs returns whether the board can be filled, it simply fill into an empty slot (at idx) with all possible digits if valid
        # on the true path, we don't backtrack because we want to return the solved board
        def dfs(idx) -> bool:
            nonlocal board
            if idx == len(empty_slots):
                # end of the game
                return True
            row, col = empty_slots[idx]
            for digit in digits:
                if isValid(row, col, digit):
                    # fill into the board
                    board[row][col] = digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[calBoxIndex(row, col)].add(digit)
                    if dfs(idx+1):
                        # solved successfully
                        return True
                    # backtrack, restore
                    board[row][col] = '.'
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    boxes[calBoxIndex(row, col)].remove(digit)
            
            # exhausted all possibilities, trim the branch
            return False

        # build all hashsets
        empty_slots = []
        for row in range(N):
            for col in range(N):
                val = board[row][col]
                if val == '.':
                    empty_slots.append((row, col))
                    continue
                rows[row].add(val)
                cols[col].add(val)
                boxes[calBoxIndex(row, col)].add(val)

        dfs(0)
        return board