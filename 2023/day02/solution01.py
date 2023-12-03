import re


def get_lines(file):
    with open(file) as f:
        lines = []
        for line in f.read().split("\n")[:-1]:
            index = line.find(":") + 1
            info = line[index:].replace(" ", "").split(";")
            info = [x.split(",") for x in info]
            lines.append(info)

        return lines


def is_valid_game(game):
    max_colors = {
        "red": 12,
        "blue": 14,
        "green": 13,
    }
    for cubes in game:
        for cube_type in cubes:
            match = re.match(r"(\d+)([a-zA-Z]+)", cube_type)
            if not match:
                continue
            number = int(match.group(1))
            color = match.group(2)

            if number > max_colors[color]:
                return False

    return True


if __name__ == "__main__":
    games = get_lines("./input01.txt")
    gameNumber = 1
    sum = 0
    for game in games:
        if is_valid_game(game):
            print(sum, gameNumber)
            sum += gameNumber

        gameNumber += 1

    print(sum)
