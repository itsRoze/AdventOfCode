from helpers import is_symbol, is_within_bounds

DIRS = [  # row, col
    (0, -1),  # top
    (1, -1),  # top right
    (1, 0),  # right
    (1, 1),  # bottom right
    (0, 1),  # bottom
    (-1, 1),  # bottom left
    (-1, 0),  # left
]


def parse_file(file):
    with open(file, "r") as f:
        schematic = f.read().split("\n")[:-1]

    L = len(schematic)
    A: list[tuple[int, int]] = []  # asteriks (row,col)
    N: list[tuple[int, tuple[int, int]]] = []  # numbers (number, (row,col) of start)

    for row, line in enumerate(schematic):
        col = 0
        while col < L:
            cell = line[col]
            if cell == "*":
                A.append((row, col))
                col += 1
            elif cell.isdigit():
                number = ""
                coord = (row, col)
                while col < L and line[col].isdigit():
                    number += line[col]
                    col += 1
                N.append((int(number), coord))
            else:
                col += 1

    return L, N, A, schematic


def get_possible_gears(
    N: list[tuple[int, tuple[int, int]]], schematic: list[str]
) -> dict[tuple[int, int], list[int]]:
    possible_gears = {}

    for number in N:
        n, coord = number
        n_row, n_col = coord

        n_str = str(n)
        # for each digit in the number, check if its next to a asterik
        for c in range(len(n_str)):
            for d in DIRS:
                row = n_row + d[0]
                col = n_col + d[1] + c
                if not is_within_bounds((row, col), schematic):
                    continue

                if schematic[row][col] == "*" and (row, col) == (n_row, n_col + c):
                    possible_gears.setdefault((row, col), []).append(n)

    return possible_gears


if __name__ == "__main__":
    L, N, A, schematic = parse_file("example01.txt")
    gears = get_possible_gears(N, schematic)
    print(gears)
