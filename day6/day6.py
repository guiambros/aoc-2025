import operator
import functools
import numpy as np


def remove_empty(input):
    return [el for el in input if el != ""]


def solution(input):  # pylint: disable=all
    input = input.splitlines()

    # extract operators
    operators = remove_empty(input[-1].split(" "))
    ops = [operator.add if op == "+" else operator.mul for op in operators]
    input = input[:-1]

    # create 2D array of operands
    numbers = np.zeros((len(input), len(ops)), dtype=int)
    for i, line in enumerate(input):
        operands = remove_empty(line.split(" "))
        for j, op in enumerate(operands):
            numbers[i][j] = int(op)

    # part 1
    answer = 0
    for coef, op in zip(numbers.T, ops):
        answer += functools.reduce(op, coef)
    print(f"Part 1: {answer}")

    # part 2
    def get_operands(input):
        num_lines = len(input)
        numbers, s, cols = [], "", 0
        while cols < len(input[0]):
            for i in range(num_lines):
                s += input[i][cols]
            if all(s[i] == " " for i in range(num_lines)):
                break
            numbers.append(int(s))
            s = ""
            cols += 1
        return [l[cols + 1 :] for l in input], numbers

    answer, i, operands = 0, 0, []
    while True:
        input, operands = get_operands(input)
        if operands == []:
            break
        answer += functools.reduce(ops[i], operands)
        i += 1
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    file = open("input_2025_6.txt", "rt", encoding="utf-8").read()
    solution(file)
