def multiple_repeated(s):
    return s in (s + s)[1:-1]


def half_repeated(s):
    half = len(s) // 2
    return s[:half] == s[half:]


def solution(input):  # pylint: disable=all
    sum_invalid_p1, sum_invalid_p2 = 0, 0

    for combination in input:
        d1, d2 = combination.split("-")
        d1, d2 = int(d1), int(d2)

        for i in range(d1, d2 + 1):
            if half_repeated(str(i)):
                sum_invalid_p1 += int(i)
            if multiple_repeated(str(i)):
                sum_invalid_p2 += int(i)

    print(f"Part 1: {sum_invalid_p1}")
    print(f"Part 2: {sum_invalid_p2}")


if __name__ == "__main__":
    file = open("input_2025_2.txt", "rt", encoding="utf-8").read()
    input = file.split(",")
    solution(input)
