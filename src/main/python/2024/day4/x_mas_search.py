input_path = '../../../resources/2024/day4'

values_f = open(input_path, 'r')

matrix = values_f.readlines()

result = 0


def i_am_a_star(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])
    if i<1 or j<1 or i+1>=rows or j+1>=rows:
        return False

    one_diagonal = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
    another_diagonal = matrix[i+1][j-1] + matrix[i][j] + matrix[i-1][j+1]

    if (one_diagonal == 'MAS' or one_diagonal == 'SAM') and (another_diagonal == 'MAS' or another_diagonal == 'SAM'):
        return True
    else:
        return False


for i in range(len(matrix)):
    for j in range(len(matrix[0])-1):
#         look only for Xes and try to match them with any starting XMAS
        current = matrix[i][j]
        print(f"Parsing at ({i},{j}): {current}")
        if current == 'A':
            print(f"Parsing A at ({i},{j})")
            # you either are a star or not...
            if i_am_a_star(matrix, i, j):
                print(f"Found a start having middle in {i},{j}")
                result += 1


print(f"Result: {result}")

