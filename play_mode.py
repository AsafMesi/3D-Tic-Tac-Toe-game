from game import Game


# assuming the input consist of numbers between 0 and 3 -> The code should work as planned.
def main():
    game = Game()
    print("Here is a blank board, lets play!")
    game.print_board()
    while not game.is_game_over():
        print(f"{game.current_player} turn.")
        x, y, z = input("Please insert 'x y z' coordinates with space between them.\n").split(' ')
        game.play_move(int(x), int(y), int(z))
        game.print_board()

    print(game.state())
    if game.winner:
        print(f"The winning sequence is: {game.winning_sequence}.")


if __name__ == "__main__":
    main()
