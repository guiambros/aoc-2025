def check_surroundings(input, x, y):
    cols = len(input[0])
    rows = len(input)
    cnt = 0
    if input[y][x] != "@" and input[y][x] != "x":
        return 0
    for dc in [-1, 0, 1]:
        for dr in [-1, 0, 1]:
            if dc == 0 and dr == 0:
                continue
            if y+dr < 0 or y+dr >= rows or x+dc < 0 or x+dc >= cols:
                continue
            if input[y+dr][x+dc] == "@" or input[y+dr][x+dc] == "x":
                cnt+=1
    if cnt < 4:
        input[y] = input[y][:x] + "x" + input[y][x + 1:]
        return 1
    return 0

def clean_input(input):
    num_removed = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == "x":
                input[y] = input[y][:x] + "." + input[y][x + 1:]
                num_removed += 1
    return input, num_removed

def remove_rolls(input):
    answer1 = 0
    c = len(input[0])
    r = len(input)
    for y in range(r):
        for x in range(c):
            if input[y][x] == "@" or input[y][x] == "x":
                answer1 += check_surroundings(input, x, y)
    return answer1

def recursive_remove_rolls(input, num_removed=None):
    answer2 = 0
    while remove_rolls(input):
        input, num_removed = clean_input(input)
        if num_removed == 0:
            break
        answer2 += num_removed
    return answer2

if __name__ == "__main__":
    file = open("input_2025_4.txt", "rt", encoding="utf-8").read()
    input = [l for l in file.splitlines()]
    
    answer1 = remove_rolls(input.copy())
    print(f"Part 1: {answer1}")
    
    answer2 = recursive_remove_rolls(input.copy())
    print(f"Part 2: {answer2}")

