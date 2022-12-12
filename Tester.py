from game import Game


def main(verbose=False):
    choice = input("Would you like to play? (y/n)\n")
    while choice == 'y':
        moves = input("Enter input sequence\n").split(' ')
        moves_iterator = iter(moves)
        game = Game()
        while not game.is_game_over():
            x = next(moves_iterator, None)
            y = next(moves_iterator, None)
            z = next(moves_iterator, None)
            if not x:
                break
            game.play_move(int(x), int(y), int(z))

        game.print_board()
        print(game.state())
        if verbose and game.winner:
            print(f"Winning sequence: {game.winning_sequence}.\n")

        choice = input("Would you like to play again? (y/n)\n")


if __name__ == "__main__":
    main(verbose=True)
