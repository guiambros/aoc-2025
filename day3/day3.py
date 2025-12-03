# brute force part 1
def all_combinations(row):
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            yield str(row[i]) + str(row[j])

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
    # part 1 - brute force
    answer = 0
    for row in input:
        comb = sorted(all_combinations(row))
        answer += int(comb[-1])
    print(f"Part 1: {answer}")

    # part 1 - generalizable method
    answer = 0
    for row in input:
        comb = get_best_batt(row, 0, 2)
        answer += int(comb)
    print(f"Part 1: {answer}")

    # part 2
    answer = 0
    for row in input:
        comb = get_best_batt(row, 0, 12)
        answer += int(comb)
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    file = open("input_2025_3.txt", "rt", encoding="utf-8").read()
    input = [l for l in file.splitlines()]  # pylint: disable=all
    solution(input)
