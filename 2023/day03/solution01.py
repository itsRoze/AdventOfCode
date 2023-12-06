from helpers import is_symbol, is_within_bounds

DIRS = [  # row, col
    (0, -1),  # top
    (1, -1),  # top right
    (1, 0),  # right
    (1, 1),  # bottom right
    (0, 1),  # bottom
    (-1, 1),  # bottom left
    (-1, 0),  # left
    (-1, -1),  # top left
]


def parse_file(file):
    with open(file, "r") as f:
        schematic = f.read().split("\n")[:-1]

    L = len(schematic)
    N: list[tuple[int, tuple[int, int]]] = []  # numbers (number, (row,col) of start)

    for row, line in enumerate(schematic):
        col = 0
        while col < L:
            cell = line[col]
            if cell.isdigit():
                number = ""
                coord = (row, col)
                while col < L and line[col].isdigit():
                    number += line[col]
                    col += 1
                N.append((int(number), coord))
            else:
                col += 1

    return L, N, schematic


def is_next_to_symbol(
    number: tuple[int, tuple[int, int]], schematic: list[str]
) -> bool:
    n, coord = number
    n_row, n_col = coord

    n_str = str(n)

    # for each digit in the number, check if its next to a symbol
    for c in range(len(n_str)):
        for d in DIRS:
            row = n_row + d[0]
            col = n_col + d[1] + c
            if not is_within_bounds((row, col), schematic):
                continue

            if is_symbol(schematic[row][col]):
                return True

    return False


def get_part_nums(N: list[tuple[int, tuple[int, int]]], schematic) -> list[int]:
    return [number[0] for number in N if is_next_to_symbol(number, schematic)]


if __name__ == "__main__":
    L, N, schematic = parse_file("input01.txt")
    parts = get_part_nums(N, schematic)
    print(sum(parts))
