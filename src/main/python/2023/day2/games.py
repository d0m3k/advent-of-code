input_path = '../../../resources/2023/day2'


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
    games_list = [x.split(', ') for x in split_games]
    is_possible = True
    for game in games_list:
        for run in game:
            count, color = run.split(" ")
            if int(count) > counts[color]:
                print(f"In game {game_num}, there is {count} of {color}. IMPOSSIBLE!")
                is_possible = False
    if is_possible:
        sum_of_games += game_num

print(f"Sum of all: {sum_of_games}")