INPUT_FILE = "input.txt"


def parse_file():
    T = ""
    R = ""

    with open(INPUT_FILE) as f:
        time = f.readline()
        time = time.replace("Time: ", "").strip().split(" ")
        T = int("".join(time))

        record = f.readline()
        record = record.replace("Distance: ", "").strip().split(" ")
        R = int("".join(record))

    return T, R


def num_ways(time: int, record: int):
    greater_than_record = 0

    for hold in range(time + 1):
        distance_traveled = hold * (time - hold)
        if distance_traveled > record:
            greater_than_record += 1

    return greater_than_record


if __name__ == "__main__":
    T, R = parse_file()
    print(num_ways(T, R))
