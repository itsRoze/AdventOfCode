# Regex
import re

# For Reduce
from functools import reduce


def get_lines(file):
    return open(file).read().splitlines()


def get_calibration(line: str):
    pattern = r"one|two|three|four|five|six|seven|eight|nine|\d"
    matches = re.findall(pattern, line)
    first = matches[0]

    pattern = r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d"
    matches = re.findall(pattern, line[::-1])
    last = matches[0][::-1]

    digits = matches_to_int([first, last])
    return int("".join(digits))


def matches_to_int(matches):
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return [word_to_number[m] if m in word_to_number else m for m in matches]


# main
if __name__ == "__main__":
    lines = get_lines("./input01.txt")
    total = 0
    for line in lines:
        c = get_calibration(line)
        print(line, c)
        total += c
    print(total)
    # get_calibration("85oneight")
    # get_calibration("two5twojjvkjbs")
    # get_calibration("8trchslhdfxxhrrkonesix74twoone")


# print(reduce(lambda x, y: x + y, calibrations))
# Tricky Cases
# 85oneightt
# two5twojjvkjbs
# 8trchslhdfxxhrrkonesix74twoone 82
