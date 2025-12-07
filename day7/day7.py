import numpy as np


def solution_p1(map):  # pylint: disable=all
    B = set()  # beams
    S = np.zeros((len(map), len(map[0])), dtype=int)  # p2 = strenght of beams
    num_splits = 0  # p1 = number of splits

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                B.add(x)
                S[y][x] = 1

            # p2: if empty space OR entering the splitter, with a beam coming through, AND the space immediately
            # above is NOT a splitter, then carry on the strength of the beam
            if (map[y][x] == "." or map[y][x] == "^") and y >= 1 and (x in B) and map[y - 1][x] != "^":
                S[y][x] += S[y - 1][x]

            # p1 and p2: if entering the splitter, with a beam coming through, then split
            if map[y][x] == "^" and (x in B):
                B.remove(x)
                num_splits += 1
                B.add(x - 1)
                B.add(x + 1)
                # p2: if splitting, then carry over the strength of the beam
                S[y + 1][x - 1] += S[y][x]
                S[y + 1][x + 1] += S[y][x]

    print(f"Part 1: {num_splits}, Part 2: {sum(S[-1])}")


if __name__ == "__main__":
    file = open("input_2025_7.txt", "rt", encoding="utf-8").read()
    map = file.split("\n")
    solution_p1(map)
