day_5_input_path = '../../resources/day-5-input'

# remember, that in this exercise, ranges must be upper-bound-inclusive (hence + 1 everywhere)

def get_line_tuple(line):
    pairs = line.split(' -> ')
    p1 = pairs[0].split(',')
    p2 = pairs[1].split(',')
    return (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))


def isLine(x):
    return x[0][0] == x[1][0] or x[0][1] == x[1][1]


def get_max(just_lines_tuples, index_inside):
    return max([x[0][index_inside] for x in just_lines_tuples] + [x[1][index_inside] for x in just_lines_tuples])


def empty_board(max_x, max_y):
    x_board = [[] for _ in range(0, max_x + 1)]
    for x in range(0, len(x_board)):
        x_board[x] = [0 for _ in range(0, max_y + 1)]
    return x_board


def draw_board(board):
    for line in board:
        print(line)


values_f = open(day_5_input_path, 'r')
values = values_f.readlines()

tuples = [get_line_tuple(x) for x in values]
print(f"{tuples}")

just_lines_tuples = [x for x in tuples if isLine(x)]
print(f"{just_lines_tuples}")

max_x = get_max(just_lines_tuples, 0)
max_y = get_max(just_lines_tuples, 1)

print(f"{max_x:}, {max_y:}")

board = empty_board(max_x, max_y)
draw_board(board)


def draw_horizontal_line(board, x1, y1, y2):
    if(y1 > y2):
        y1, y2 = y2, y1
    for y in range(y1, y2+1):
        board[x1][y] += 1


def draw_vertical_line(board, y1, x1, x2):
    if(x1 > x2):
        x1, x2 = x2, x1
    for x in range(x1, x2+1):
        board[x][y1] += 1


for (x1, y1), (x2, y2) in just_lines_tuples:
    if x1 == x2:
        print(f'Drawing horizontal for x={x1}, y=({y1},{y2})')
        draw_horizontal_line(board, x1, y1, y2)
    if y1 == y2:
        print(f'Drawing vertical for y={y1}, x=({x1},{x2})')
        draw_vertical_line(board, y1, x1, x2)



print("new board:")
draw_board(board)


def overlaps(board, how_many_lines):
    result = 0
    for line in board:
        for x in line:
            if x >= how_many_lines:
                result += 1
    return result


print(f"Overlapping points: {overlaps(board, 2)}")