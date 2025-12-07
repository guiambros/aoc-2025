from collections import defaultdict

import numpy as np


class beams:
    def __init__(self):
        self.current = set()

    def add(self, x, strength=1):
        if not x in self.current:
            self.current.add(x)
            return 1
        return 0

    def exists(self, x):
        return x in self.current

    def remove(self, x):
        if x in self.current:
            self.current.remove(x)
            return True
        return False

    def add_node_to_history(self, node):
        if not node in self.history:
            self.history.append(self.history + [node])


def solution_p1(map):  # pylint: disable=all
    # part 1
    answer = 0
    B = beams()
    num_splits = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                B.add(x)
            if map[y][x] == "^":
                found = B.remove(x)
                if found:
                    num_splits += 1
                    B.add(x - 1)
                    B.add(x + 1)

    print(f"Part 1: {num_splits}")


def solution_p2(map):  # pylint: disable=all
    # part 2
    answer = 0
    B = beams()
    M = np.zeros((len(map), len(map[0])), dtype=int)

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "S":
                B.add(x)
                M[y][x] = 1
            elif (map[y][x] == "." or map[y][x] == "^") and y >= 1 and B.exists(x) and map[y - 1][x] != "^":
                M[y][x] += M[y - 1][x]

            if map[y][x] == "^" and B.exists(x):
                M[y + 1][x - 1] += M[y][x]
                M[y + 1][x + 1] += M[y][x]
                B.add(x - 1)
                B.add(x + 1)

    print(f"Part 2: {sum(M[-1])}")


if __name__ == "__main__":
    file = open("input_2025_7.txt", "rt", encoding="utf-8").read()
    map = file.split("\n")
    solution_p1(map)
    solution_p2(map)
