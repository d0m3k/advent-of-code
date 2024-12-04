input_path = '../../../resources/2024/day4'

values_f = open(input_path, 'r')

matrix = values_f.readlines()


# I admit - Chat wrote the better version XD
def find_word_in_matrix(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])  # Dimensions of the matrix
    directions = [
        (-1, -1), (-1, 1),  # Up-left, Up-right
        (1, -1), (1, 1),    # Down-left, Down-right
        (1, 0), (-1, 0),    # Down, Up
        (0, 1), (0, -1)     # Right, Left
    ]

    found_words = []

    for dx, dy in directions:
        word = []
        x, y = i, j
        for _ in range(4):  # Collect 4 characters in the current direction
            if 0 <= x < rows and 0 <= y < cols:  # Stay within bounds
                word.append(matrix[x][y])
                x += dx
                y += dy
            else:
                break  # Stop if out of bounds

        if len(word) == 4:  # Check if the word is 4 characters long
            found_words.append(''.join(word))

    return found_words

result = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])-1):
        print(f"Parsing at ({i},{j})")
        words = find_word_in_matrix(matrix, i, j)
        for word in words:
            if word == 'XMAS':
                result += 1

print(f"Result: {result}")

