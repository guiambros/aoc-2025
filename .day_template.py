import time
import numpy as np
from collections import defaultdict


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result

    return wrapper


def solution(input):  # pylint: disable=all
    # part 1
    answer = 0
    print(f"Part 1: {answer}")

    # part 2
    answer = 0
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    file = open("input_2025_x.txt", "rt", encoding="utf-8").read()
    # file = open("test.txt", "rt", encoding="utf-8").read()

    # -- each row w/ one alphanumerical element - e.g ["ABC", "DEF", "GHI"]
    input = [l for l in file.splitlines()]  # pylint: disable=all

    # -- each row w/ multiple numbers: e.g. "10, 11, 12\n13, 14, 15" -> [[10, 11, 12], [13, 14, 15]]
    # -- adjust delimiter as needed
    # input = [[int(c) for c in row.split(" ")] for row in input] # for single space separator
    # input = [[int(c) for c in row.split()] for row in input]    # for multiple spaces separator

    # -- each row w/ a single long line with alpha, csv format - e.g. "ABC,DEF,GHI" -> ["ABC", "DEF", "GHI"]
    # -- adjust delimiter as needed
    # input = [line for line in input.split(",")]

    # -- each row w/ a single long line with numbers, csv format - e.g. "1,2,3" -> [1, 2, 3]
    # -- adjust delimiter as needed
    # input = [int(i) for i in input.split(",")]

    solution(input)
