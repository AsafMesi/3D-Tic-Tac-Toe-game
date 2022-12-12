import random
from game import Game

input_file = "input.txt"
results_file = "result.txt"
problems_to_generate = 10


class ListPopper:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if not self.lst:
            raise StopIteration
        return self.lst.pop()


def get_all_triplets():
    all_triplets = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                all_triplets.append(f"{str(i)} {str(j)} {str(k)}")
    random.shuffle(all_triplets)
    return all_triplets


def write_to_file(file, sequence, addition):
    with open(file, 'a') as f:
        f.write(f'{sequence}')
        f.write(f'{addition}\n')


def generate_problem(i):
    moves_iterator = ListPopper(get_all_triplets())
    game = Game()
    sequence = []
    while not game.is_game_over():
        move = next(moves_iterator, None)
        x, y, z = move.split(' ')
        game.play_move(int(x), int(y), int(z))
        sequence.append(move)
    sequence = ' '.join(sequence)
    write_to_file(input_file, sequence, '\ny')
    write_to_file(results_file, f"{i}: {game.state()} {game.winning_sequence}", "")


def main():
    for i in range(2, (2 * problems_to_generate + 2), 2):
        generate_problem(i)
    return 0


def add_tie():
    i = 0
    while True:
        i += 1
        game = Game()
        sequence = []
        moves_iterator = ListPopper(get_all_triplets())
        while not game.is_game_over():
            move = next(moves_iterator, None)
            x, y, z = move.split(' ')
            game.play_move(int(x), int(y), int(z))
            sequence.append(move)

        if game.moves_count == game.board_size**3:
            sequence = ' '.join(sequence)
            write_to_file(input_file, sequence, '\ny')
            write_to_file(results_file, f"Special: {game.state()} {game.winning_sequence}", "")
            break
        print(i)


if __name__ == "__main__":
    main()
    # add_tie()
