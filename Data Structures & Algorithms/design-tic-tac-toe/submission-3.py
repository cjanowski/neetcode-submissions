class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antiDiagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 1 else - 1
        n = len(self.rows)

        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer

        if row == col:
            self.diagonal += currentPlayer
        
        if row + col == n - 1:
            self.antiDiagonal += currentPlayer

        if (abs(self.rows[row]) == n or
            abs(self.cols[col]) == n or
            abs(self.diagonal) == n or
            abs(self.antiDiagonal) == n):
            return player

        return 0