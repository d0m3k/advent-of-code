day_13_input_path = '../../../resources/y2021/day-13-input'


def get_dots(line):
   s = line.split(',')
   return int(s[0]), int(s[1])


def get_first_fold(values):
   for line in lines:
      if 'along' in line:
         tuple = line.split(' ')[2].split('=')
         return tuple[0], int(tuple[1])


def get_fold(line):
   tuple = line.split(' ')[2].split('=')
   return tuple[0], int(tuple[1])



values_f = open(day_13_input_path, 'r')
lines = values_f.readlines()

dots = [get_dots(line) for line in lines if ',' in line]
# direction, fold_line_coordinate = get_first_fold(lines)

folds = [get_fold(line) for line in lines if 'along' in line]

# print(f"Got dots {dots}, fold: {direction}, {fold_line_coordinate}")
print(f"Got dots {dots}, folds: {folds}")

# fold should work as follows:
# line that folds goes to waste
# the (width/length) becomes fold_line_coordinate
# values below (to the right/down) should have their one coordinate changed such that:
# if folding y, x stays constant, and y is fold_line_coordinate - (ponint_y - fold_line_coordinate)
# same for x
for direction, fold_line_coordinate in folds:
   for i in range(0, len(dots)):
      x, y = dots[i]
      if direction == 'x' and x > fold_line_coordinate:
         dots[i] = (fold_line_coordinate - (x - fold_line_coordinate), y)
      if direction == 'y' and y > fold_line_coordinate:
         dots[i] = (x, fold_line_coordinate - (y - fold_line_coordinate))


def print_dots(result_set):
   max_x = max([x for x, _ in result_set])
   max_y = max([y for _, y in result_set])
   print(f"We could have like {max_x},{max_y} thing")
   matrix = [['.' for x in range(max_x+1)] for y in range(max_y+1)]
   print(f"Got matrix x={len(matrix)} y={len(matrix[0])}")
   for y,x in result_set:
      print(f"Adding value {x}, {y}")
      matrix[x][y] = "#"

   for line in matrix:
      for char in line:
         print(char, end='')
      print()


result_set = {dot for dot in dots}
print(f"Got {result_set}, size: {len(result_set)}")
print_dots(result_set)
