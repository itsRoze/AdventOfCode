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


def get_power(game):
    cubes = {"red": 0, "green": 0, "blue": 0}

    for round in game:
        for cube_type in round:
            match = re.match(r"(\d+)([a-zA-Z]+)", cube_type)
            if not match:
                continue
            number = int(match.group(1))
            color = match.group(2)
            if number > cubes[color]:
                cubes[color] = number
    return cubes["red"] * cubes["green"] * cubes["blue"]


if __name__ == "__main__":
    games = get_lines("./input01.txt")
    sum = 0
    for g in games:
        power = get_power(g)
        sum += power
    print(sum)
