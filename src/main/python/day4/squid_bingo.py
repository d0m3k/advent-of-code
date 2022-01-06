import itertools
from functools import reduce

day_4_input_path = '../../resources/day-4-input'

values_f = open(day_4_input_path, 'r')
values = values_f.readlines()

BOARD_WIDTH = 5

# for checking whether we won or not, we need to only count if any of
#  columns / rows got its count to 5

boards = []
for i in range(0, len(values)):
    current = values[i]
    if i == 0:
        numbers = [x.strip() for x in current.split(',')]
    elif not current.strip():
        if 'current_board' in locals():
            boards.append(current_board)
        current_board = []
    else:
        current_board.append([(x, False) for x in current.split()])

# add last one, because for loop is not friendly
boards.append(current_board)

# and let's count boards, so we can assume we are finding bingo boards till the last one comes
bingoed_already = set() # you could not just count, because board can easily "bingo" more than once before another bingoes
bingo_max = len(boards)

print("Numbers we have: {}, boards: {}".format(numbers, boards))


# dear god, what an awful complexity ;)
def find_bingo_table(bingoed_already, bingo_max):
    for current_number in numbers:
        print("Marking {}...".format(current_number))
        for board_i in range(0, len(boards)):
            board = boards[board_i]
            for row_i in range(0, len(board)):
                row = board[row_i]
                for field_i in range(0, len(row)):
                    field = row[field_i]
                    if field[0] == current_number:
                        print("Marking field!")
                        row[field_i] = (field[0], True)

                        # check for bingo
                        # rowcheck is simple:
                        if check_rows(row) or check_columns(board, field_i):
                            print("Hit the bingo in {} (0-indexed) table while getting {}!".format(board_i,
                                                                                                   current_number))
                            bingoed_already.add(board_i)
                            if len(bingoed_already) == bingo_max:
                                return board_i, current_number


def check_rows(row):
    return len([x for x in row if x[1] is True]) == BOARD_WIDTH


def check_columns(board, field_i):
    res = []
    for row_i in range(0, len(board)):
        res.append(board[row_i][field_i])
    return len([x for x in res if x[1] is True]) == BOARD_WIDTH


# you can get to the first part result by setting bingo_max to 1
bingo_index, bingo_number = find_bingo_table(bingoed_already, bingo_max)

print("Numbers we have: {}, boards: {}".format(numbers, boards))


def score_board(bingo_index, bingo_number):
    flat_list = list(itertools.chain.from_iterable(boards[bingo_index]))
    print("List of {} table is: {}".format(bingo_index, flat_list))
    unmarked_sum = reduce(int.__add__, [int(x[0]) for x in flat_list if not x[1]])
    print(f"So the result is {bingo_number} * {unmarked_sum} = { int(bingo_number) * unmarked_sum }")



score_board(bingo_index, bingo_number)