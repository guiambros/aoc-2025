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
    dial, inc = 50, 0    
    pwd, pwd2 = 0, 0
    
    for rot in input:
        # parse input
        if rot[0] == "L":
            inc = -int(rot[1:])
        else:
            inc = int(rot[1:])

        # part 2
        if (dial > 0 and (dial+inc) < 0) or (dial < 0 and (dial+inc) > 0) or ((dial+inc) == 0): # if we crossed or at zero
            pwd2 += 1
        pwd2 += abs(dial+inc) // 100 # how many times we passed zero

        # part 1
        dial += inc
        if dial < 0:
            dial += 100
        dial = dial % 100
        if dial == 0:
            pwd += 1
    
    print(f"Part 1: {pwd}")
    print(f"Part 2: {pwd2}")


if __name__ == "__main__":
    file = open("input_2025_1.txt", "rt", encoding="utf-8").read()
    # file = open("test.txt", "rt", encoding="utf-8").read()

    # -- each row w/ one alphanumerical element - e.g ["ABC", "DEF", "GHI"]
    input = [l for l in file.splitlines()]  # pylint: disable=all
    

    # -- each row w/ multiple numbers: e.g. "10, 11, 12\n13, 14, 15" -> [[10, 11, 12], [13, 14, 15]]
    # -- adjust delimiter as needed
    # input = [[int(c) for c in row.split(" ")] for row in input]

    # -- each row w/ a single long line with alpha, csv format - e.g. "ABC,DEF,GHI" -> ["ABC", "DEF", "GHI"]
    # -- adjust delimiter as needed
    # input = [line for line in input.split(",")]

    # -- each row w/ a single long line with numbers, csv format - e.g. "1,2,3" -> [1, 2, 3]
    # -- adjust delimiter as needed
    # input = [int(i) for i in input.split(",")]

    solution(input)
