import re

INPUT_FILE = "input01.txt"


def parse_file():
    S = []  # (winning_nums, given_nums)[]
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
            S.append((winning_nums, given_nums))
        else:
            print("No digit found after the colon.")

    return S


# O(min(N, M))
def get_matches(card: tuple[list[str], list[str]]) -> int:
    winning = set(card[0])
    given = set(card[1])

    intersection = winning & given
    return len(intersection)


# O(C * min(N, M))
def get_matches_map(S):
    M = {}  # card: matches
    card_num = 1
    for s in S:
        matches = get_matches(s)
        M[card_num] = matches
        card_num += 1

    return M


def get_copies(M: dict[int, int]):
    keys = M.keys()
    C = {key: 1 for key in keys}

    for m_k, m_v in M.items():
        for _ in range(C[m_k]):
            for i in range(1, m_v + 1):
                if (m_k + i) in C:
                    C[m_k + i] += 1

    return C


if __name__ == "__main__":
    S = parse_file()
    M = get_matches_map(S)
    C = get_copies(M)

    total = 0
    for k, v in C.items():
        total += v
    print(total)
