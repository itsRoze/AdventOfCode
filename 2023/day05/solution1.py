INPUT_FILE = "input.txt"


def parse_file():
    seeds = []
    maps = []
    with open(INPUT_FILE, "r") as f:
        seeds = f.readline()
        seedsIdx = seeds.find(":")
        seeds = seeds[seedsIdx + 2 :].strip().split(" ")
        current_map = []
        for line in f:
            if line.strip() == "":
                continue

            if line[0].isdigit():
                current_map.append(line.strip().split(" "))
            else:
                if len(current_map) > 0:
                    maps.append(current_map)
                    current_map = []

        maps.append(current_map)

    S = [int(x) for x in seeds]
    M = [[[int(y) for y in x] for x in y] for y in maps]
    return S, M


def get_location(seed, M):
    last_value = seed
    for m in M:
        new_value = None
        for arr in m:
            if (new_value is None) and (arr[1] <= last_value < arr[1] + arr[2]):
                new_value = last_value - arr[1] + arr[0]
                break
        if new_value is None:
            new_value = last_value
        last_value = new_value

    return last_value


def get_locations(S, M):
    L = []
    for seed in S:
        L.append(get_location(seed, M))

    return L


if __name__ == "__main__":
    S, M = parse_file()
    L = get_locations(S, M)
    print(min(L))
