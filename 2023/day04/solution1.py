import re

INPUT_FILE = "input01.txt"


def parse_file():
    C = []  # (winning_nums, given_nums)[]
    cards = []
    with open(INPUT_FILE, "r") as f:
        cards = f.readlines()

    # Define the pattern to match the first digit after the colon
    pattern = r":\D*(\d)"
    for card in cards:
        match = re.search(pattern, card)
        if match:
            # Get the index of the matched digit
            first_digit_index = match.start(1)
            card = card[first_digit_index:]
            pipe = card.find("|")

            winning_nums = card[: pipe - 1]
            given_nums = card[pipe + 2 :]

            nums_pattern = r"\b\d+\b"
            winning_nums = re.findall(nums_pattern, winning_nums)
            given_nums = re.findall(nums_pattern, given_nums)
            C.append((winning_nums, given_nums))
        else:
            print("No digit found after the colon.")

    return C


# O(min(N, M))
def get_points(card: tuple[list[str], list[str]]) -> int:
    winning = set(card[0])
    given = set(card[1])

    intersection = winning & given
    if len(intersection) == 0:
        return 0

    pts = 1
    for i in range(len(intersection) - 1):
        pts *= 2
    return pts


# O(C * min(N, M))
def get_total_points(C):
    total = 0
    for c in C:
        print(c)
        pts = get_points(c)
        total += pts
    return total


if __name__ == "__main__":
    C = parse_file()
    print(get_total_points(C))
