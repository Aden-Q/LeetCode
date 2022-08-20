class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]
        # x: "A"
        # o: "B"
        flag = True
        for row, col in moves:
            if flag:
                board[row][col] = "A"
            else:
                board[row][col] = "B"
            flag = not flag
        
        # Check row, 0, 1, 2
        for row in range(3):
            if board[row][0] == "":
                continue
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                # One player win
                return board[row][0]
        
        # Check col, 0, 1, 2
        for col in range(3):
            if board[0][col] == "":
                continue
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                # One player win
                return board[0][col]
        
        # Check diagonal
        if board[0][0] != "" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]
        
        # Check anti-diagonal
        if board[0][2] != "" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]
        
        if len(moves) < 9:
            return "Pending"
        return "Draw"