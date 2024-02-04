from tictactoe.board import BoardInvalidMove
from tictactoe.game import Game


def main():

    game = None

    # Prompt User for Board Size
    while True:
        try:
            board_size = input("Select the NxN Board Size (N >= 3): ")
            board_size = int(board_size)
            game = Game(board_size, player1='Bob', player2='Alice', blank_label=" ")
            break
        except ValueError as e:
            print(e)
            print()
            continue

    game.print_game_state()

    print("Please enter a move by giving 2 valid integers separated by space, e.g. 2 0\n"
          "where 2 is the row and 0 is the column.")

    while True:
        try:
            game_iteration_msg = f"Game Iteration: {game.game_iteration}"
            print("=" * len(game_iteration_msg))
            print(game_iteration_msg)

            move = input(f"Please enter move for Player '{game.current_player}' using i j >> ")
            move = move.split(' ')

            if len(move) != 2:
                print("Please enter 2 valid integers for a move.")
                continue

            row, col = map(int, move)

            result: str | None = game.move(row, col)
            print(f"Result: {result}")
            if result in game.players:
                print(f"Winner: {game.winner}")
                game.print_game_state()
                exit(0)
            elif result == "finished":
                print("No one won.")
                game.print_game_state()
                exit(0)
            else:
                print("State of Game:")
                game.print_game_state()
                print(f"Scores: {game.board.scores}")
                print(f"Available Moves: {game.board.valid_moves()}")
                print()
                continue

        except ValueError as e:
            print(e, "\n")
            continue

        except BoardInvalidMove as e:
            print(e, "\n")
            continue

        except KeyboardInterrupt:
            print("Goodbye!")
            exit(0)


if __name__ == "__main__":
    main()
