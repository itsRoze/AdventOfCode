INPUT_FILE = "input.txt"


def parse_file():
    T = []
    R = []

    with open(INPUT_FILE) as f:
        times = f.readline()
        times = times.replace("Time: ", "").strip().split(" ")
        T = [int(x) for x in times if x.isdigit()]

        records = f.readline()
        records = records.replace("Distance: ", "").strip().split(" ")
        R = [int(x) for x in records if x.isdigit()]

    return T, R


def num_ways(time: int, record: int):
    greater_than_record = 0

    for hold in range(time + 1):
        distance_traveled = hold * (time - hold)
        if distance_traveled > record:
            greater_than_record += 1

    return greater_than_record


def get_total_ways(T: list, R: list):
    total = 1
    for time, record in zip(T, R):
        total *= num_ways(time, record)

    return total


if __name__ == "__main__":
    T, R = parse_file()
    print(get_total_ways(T, R))
