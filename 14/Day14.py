with open('/Users/cturner/personal/advent-of-code-23/14/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

ROCK = "O"
STONE = "#"
SPACE = "."

def is_space(x, y):
    return x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines) and lines[y][x] == SPACE

def check_stone(lines, x, y):
    if lines[y][x] == ROCK:
        can_move_to = None
        for k in range(1,y+1):
            if is_space(x, y-k):
                can_move_to = (x, y-k)
            else:
                break
        if can_move_to is not None:
            move_x, move_y = can_move_to
            lines[move_y] = lines[move_y][:move_x] + ROCK + lines[move_y][move_x+1:]
            lines[y] = lines[y][:x] + SPACE + lines[y][x+1:]
    return lines

def cycle(lines):
    for y in range(1, len(lines)):
        for x in range(len(lines[y])):
            lines = check_stone(lines, x, y)
    return lines

cache = dict()
loop = 0
count = 0
for c in range(0,1000000001):
    count += 1
    lines = cycle(lines)
    for i in range(3):
        lines = ["".join(reversed(list(x))) for x in zip(*lines)]

        lines = cycle(lines)
    lines = ["".join(reversed(list(x))) for x in zip(*lines)]

    print("\n".join(lines))
    print()
    if "".join(lines) in cache.keys():
        start = cache.get("".join(lines)) 
        print(f"FOUND {c} - {start}")
        loop = c - start
        break
    cache["".join(lines)] = c

remaining = (1000000000 - start)
additional_loops = remaining % loop
for _ in range(additional_loops-1):
    lines = cycle(lines)
    for i in range(3):
        count += 1
        lines = ["".join(reversed(list(x))) for x in zip(*lines)]
        lines = cycle(lines)
    lines = ["".join(reversed(list(x))) for x in zip(*lines)]
    
# print("\n".join(lines))
total = 0
for i in range(len(lines)):
    # print(f"{i}: {lines[i].count(ROCK)} - {len(lines) - i}")
    total += lines[i].count(ROCK) * (len(lines) - i)
print(total)
