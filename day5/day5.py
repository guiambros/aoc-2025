def dedup_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for r in intervals:
        if not merged or merged[-1][1] < r[0]:
            merged.append(r)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
    return merged


def solution(input):  # pylint: disable=all
    dbs, ing = input.split("\n\n")
    dbs = dbs.splitlines()
    ing = ing.splitlines()
    ing = [int(i) for i in ing]

    # part 1
    db = []
    answer = 0
    for interval in dbs:
        interval = interval.split("-")
        db.append((int(interval[0]), int(interval[1])))

    for n in ing:
        found = False
        for interval in db:
            if interval[0] <= n <= interval[1]:
                answer += 1 if not found else 0
                found = True
    print(f"Part 1: {answer}")

    # part 2
    answer2 = 0
    db = dedup_intervals(db)
    for r in db:
        answer2 += r[1] - r[0] + 1
    print(f"Part 2: {answer2}")


if __name__ == "__main__":
    file = open("input_2025_5.txt", "rt", encoding="utf-8").read()
    solution(file)
