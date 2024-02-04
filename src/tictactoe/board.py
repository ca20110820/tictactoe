from typing import List, Tuple
from itertools import permutations


class BoardInvalidMove(Exception):
    pass


class Board:

    MOVES = ['X', 'O']

    def __init__(self, board_size: int, blank_label="?"):
        if not isinstance(board_size, int):
            raise ValueError("The Board Size must be a valid Integer.")
        if board_size < 3:
            raise ValueError("The Board Size cannot be less than 3.")

        self._blank_label = blank_label

        self.board_size = board_size
        self._grid = [[self._blank_label for _ in range(self.board_size)] for _ in range(self.board_size)]

    @property
    def is_board_filled(self) -> bool:
        return all([elem in self.MOVES for row_ls in self._grid for elem in row_ls])
    
    @property
    def scores(self):
        return self._options('X'), self._options('O')

    @property
    def grid(self):
        return self._grid

    def valid_moves(self) -> List[Tuple[int, int]]:
        return [(row, col) for row, col in permutations(range(self.board_size), 2) if
                self._grid[row][col] == self._blank_label] + \
            [(i, i) for i in range(self.board_size) if self._grid[i][i] == self._blank_label]

    def get_column(self, col: int) -> list:
        if 0 > col or col > self.board_size - 1:
            raise ValueError(f"Column must be in between [0, {self.board_size - 1}]")

        return [row[col] for row in self._grid]

    def get_row(self, row: int) -> list:
        if 0 > row or row > self.board_size - 1:
            raise ValueError(f"Row must be in between [0, {self.board_size - 1}]")

        return self._grid[row]

    def get_diagonal(self, which_diagonal: int) -> list:
        # which_diagonal=1 <==> From Top Left to Bottom Right
        # which_diagonal=2 <==> From Top Right to Bottom Left

        if which_diagonal not in [1, 2]:
            raise ValueError("Value must be 1 or 2.\n1 <==> From Top Left to Bottom Right\n"
                             "2 <==> From Top Right to Bottom Left")

        if which_diagonal == 1:
            return [self._grid[i][i] for i in range(self.board_size)]

        else:
            return [self._grid[i][self.board_size - 1 - i] for i in range(self.board_size)]
            # out_list = []
            # for i in range(self.board_size):
            #     out_list.append(self._grid[i][self.board_size - 1 - i])
            # return out_list

    def _options(self, move: str) -> int:
        # Def: "Options" for X is the number of diagonals, verticals, and horizontals such that
        # the elements are either X or ?.

        # The "options" for each state of the game is changing, the more option a move is, the higher the score
        # therefore, the higher the chance of winning.

        # We can use this notion to quantify the "score" of a player. This will be useful for Machine Learning.

        if move not in self.MOVES:
            raise ValueError("The move must either be labels 'X' or 'O'.")

        option_count = 0

        for i in range(self.board_size):
            row = self.get_row(i)
            col = self.get_column(i)
            if all([elem in [move, self._blank_label] for elem in row]):
                option_count += 1

            if all([elem in [move, self._blank_label] for elem in col]):
                option_count += 1

        if all([elem in [move, self._blank_label] for elem in self.get_diagonal(1)]):
            option_count += 1

        if all([elem in [move, self._blank_label] for elem in self.get_diagonal(2)]):
            option_count += 1

        return option_count

    def print_grid(self) -> None:
        horizontal_separator = "-" * (self.board_size + (self.board_size - 1))

        for row in self._grid:
            print(horizontal_separator)
            print("|".join(row))

        print(horizontal_separator)

    def update_grid(self, move: str, row: int, col: int) -> None:
        # Check Valid Move
        # e.g. If coordinate (0, 0) is anything other than '?', then throw error.
        if move not in self.MOVES:
            raise ValueError("A Move must either be 'X' or 'O'.")
        for dim in [row, col]:
            if 0 > dim or dim > self.board_size - 1:
                raise BoardInvalidMove(f"Row or Column must be in between [0, {self.board_size - 1}]")
        if self._grid[row][col] != self._blank_label:
            raise BoardInvalidMove(f"Coordinate ({row}, {col}) has value '{self._grid[row][col]}'")

        assert self._grid[row][
                   col] == self._blank_label, f"Coordinate ({row}, {col}) has value '{self._grid[row][col]}'"

        self._grid[row][col] = move

    def check_win(self) -> str | None:
        """Check the current state of board and see if there's a winner."""
        # Check Diagonals
        for diagonal in [1, 2]:
            for move in self.MOVES:
                if all([elem == move for elem in self.get_diagonal(diagonal)]):
                    return move

        # Check Horizontals (Rows)
        for row_ls in self._grid:
            for move in self.MOVES:
                if all([elem == move for elem in row_ls]):
                    return move

        # Check Verticals (Columns)
        for col in range(self.board_size):
            for move in self.MOVES:
                if all([elem == move for elem in self.get_column(col)]):
                    return move
