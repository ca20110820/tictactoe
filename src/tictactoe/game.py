from __future__ import annotations

from tictactoe.board import Board, BoardInvalidMove


class Game:
    def __init__(self, board_size=3, player1: str = "player1", player2: str = "player2", blank_label="?"):
        self._winner = None
        self._player = player1  # Initial player will always be player1
        self._game_iteration = 0

        self.player1 = player1
        self.player2 = player2
        self.player_moves = {player1: "X", player2: "O"}  # Player Name and their associated Move Labels

        self.board = Board(board_size, blank_label=blank_label)

    @property
    def winner(self):
        return self._winner

    @property
    def players(self):
        return [self.player1, self.player2]

    @property
    def current_player(self):
        return self._player

    @property
    def game_iteration(self):
        return self._game_iteration

    def _update_game_iteration(self):
        self._game_iteration += 1

    def _update_player(self):
        self._player = self.player1 if self._player == self.player2 else self.player2

    def print_game_state(self):
        self.board.print_grid()

    def move(self, row: int, col: int) -> str | None:
        # Returns: {self.player1, self.player2, 'finished', None}

        if isinstance(self.winner, str):
            raise BoardInvalidMove(f"There's already a winner for this game instance (Player: '{self.winner}').")

        self.board.update_grid(self.player_moves[self.current_player], row, col)

        winning_move = self.board.check_win()  # X, O, or None
        if isinstance(winning_move, str):
            self._winner = self.player1 if winning_move == "X" else self.player2
            self._update_game_iteration()
            return self._winner

        if self.board.is_board_filled:
            # Return 'finished' when no one won the game.
            self._update_game_iteration()
            return "finished"

        # TODO: Collect Data here before updating the state of the game.
        # ...

        self._update_player()
        self._update_game_iteration()
