import unittest

from tictactoe.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        board_size = 3

        self.player1 = 'Bob'
        self.player2 = 'Alice'
        self.game = Game(board_size, player1=self.player1, player2=self.player2)

    @staticmethod
    def alternate_tuples(list1, list2):
        result = []
        max_len = max(len(list1), len(list2))

        for i in range(max_len):
            if i < len(list1):
                result.append(list1[i])
            if i < len(list2):
                result.append(list2[i])

        return result

    def test_game_properties(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.players[0], self.game.player1)
        self.assertEqual(self.game.players[1], self.game.player2)

    @staticmethod
    def game_scenario(test_case, player1_moves, player2_moves):
        sequential_moves = test_case.alternate_tuples(player1_moves, player2_moves)

        counter = 0
        for row, col in sequential_moves:
            if counter % 2 == 0:
                test_case.assertEqual(test_case.game.current_player, test_case.game.player1)
            else:
                test_case.assertEqual(test_case.game.current_player, test_case.game.player2)

            test_case.game.move(row, col)
            counter += 1

        test_case.assertEqual(counter, test_case.game.game_iteration)

    def test_player1_wins(self):
        # Remind: Player 1 always make the first move
        player1_moves = [(0, 0), (1, 0), (2, 0)]
        player2_moves = [(0, 1), (1, 1)]
        self.game_scenario(self, player1_moves, player2_moves)
        self.assertEqual(self.game.winner, self.player1)

    def test_player2_wins(self):
        player1_moves = [(0, 1), (1, 1), (0, 2)]
        player2_moves = [(0, 0), (1, 0), (2, 0)]
        self.game_scenario(self, player1_moves, player2_moves)
        self.assertEqual(self.game.winner, self.player2)

    def test_no_winner(self):
        player1_moves = [(0, 0), (1, 0), (2, 1), (0, 2), (2, 2)]
        player2_moves = [(2, 0), (0, 1), (1, 1), (1, 2)]
        self.game_scenario(self, player1_moves, player2_moves)
        self.assertEqual(self.game.winner, None)


if __name__ == "__main__":
    unittest.main()
