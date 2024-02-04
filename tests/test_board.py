import unittest

from tictactoe.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)

    def test_invalid_board_size(self):
        for i in [-1, 0, 1, 2]:
            self.assertRaises(ValueError, self.board.__init__, i)

    def test_get_row(self):
        for i in range(self.board.board_size):
            row = self.board.get_row(i)
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), self.board.board_size)

    def test_get_column(self):
        for i in range(self.board.board_size):
            col = self.board.get_column(i)
            self.assertIsInstance(col, list)
            self.assertEqual(len(col), self.board.board_size)

    def test_get_diagonal(self):
        for i in [1, 2]:
            diagonal = self.board.get_diagonal(i)
            self.assertIsInstance(diagonal, list)
            self.assertEqual(len(diagonal), self.board.board_size)

    def test_check_win(self):
        move = 'X'
        winning_moves = [(0, 0), (1, 0), (2, 0)]
        for i, j in winning_moves:
            self.board.update_grid(move, i, j)

        result = self.board.check_win()
        self.assertIsInstance(result, str)
        self.assertEqual(result, move)


if __name__ == "__main__":
    unittest.main()
