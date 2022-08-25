class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row_scores = [0] * n
        self.col_scores = [0] * n
        self.diag_score = 0
        self.antidiag_score = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.row_scores[row] += 1
            if self.row_scores[row] == self.n:
                return player
            self.col_scores[col] += 1
            if self.col_scores[col] == self.n:
                return player
            if row == col:
                self.diag_score += 1
            if self.diag_score == self.n:
                return player
            if row + col == self.n - 1:
                self.antidiag_score += 1
            if self.antidiag_score == self.n:
                return player
            
        if player == 2:
            self.row_scores[row] -= 1
            if self.row_scores[row] == -self.n:
                return player
            self.col_scores[col] -= 1
            if self.col_scores[col] == -self.n:
                return player
            if row == col:
                self.diag_score -= 1
            if self.diag_score == -self.n:
                return player
            if row + col == self.n - 1:
                self.antidiag_score -= 1
            if self.antidiag_score == -self.n:
                return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)