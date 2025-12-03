def get_highest_number_from_slice(slice):
    slice = [int(s) for s in slice]
    return sorted(slice)[-1]

def get_best_batt(row, start, n):
    if n == 0 or row == '' :
        return ""
    end = len(row) - n + 1
    highest = get_highest_number_from_slice(row[start:end])
    index_highest = row[start:end].index(str(highest))
    start += index_highest + 1
    return str(highest) + get_best_batt(row[start:], 0, n-1)

def solution(input):  # pylint: disable=all
    # part 1
    batteries = [int(get_best_batt(row, 0, 2)) for row in input]
    print(f"Part 1: {sum(batteries)}")

    # part 2
    batteries = [int(get_best_batt(row, 0, 12)) for row in input]
    print(f"Part 2: {sum(batteries)}")

if __name__ == "__main__":
    file = open("input_2025_3.txt", "rt", encoding="utf-8").read()
    input = [l for l in file.splitlines()]  # pylint: disable=all
    solution(input)
