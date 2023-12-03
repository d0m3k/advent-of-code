input_path = '../../../resources/2023/day2e'


values_f = open(input_path, 'r')

counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum_of_games = 0

for line in values_f.readlines():
    game_num_s, games = line.split(":")
    game_num = int(game_num_s.split(" ")[1])
    split_games = [x.strip() for x in games.strip().split(";")]
    print(f"Gejms: {game_num};;; {split_games}")

print(f"Sum of all: {sum_of_games}")