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


def get_adjacent_nums(coord: tuple[int, int], schematic: list[str]) -> bool:
    row, col = coord
    pts = set()
    for d in DIRS:
        r_x = row + d[0]
        c_x = col + d[1]

        if not is_within_bounds((r_x, c_x), schematic):
            continue
        if schematic[r_x][c_x].isdigit():
            pts.add(schematic[r_x][c_x])

    return len(pts) >= 2


def is_symbol(c: str) -> bool:
    return not c.isdigit() and c != "."


def is_within_bounds(coord: tuple[int, int], schematic: list[str]) -> bool:
    row, col = coord
    return 0 <= row < len(schematic) and 0 <= col < len(schematic[row])
