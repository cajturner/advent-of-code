with open('/Users/cturner/personal/advent-of-code-23/11/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


empty_rows = []
for i in range(0, len(lines)):
    line = lines[i]
    if line.count(".") == len(line):
        empty_rows.append(i)


empty_columns = []
for index in range(0, len(lines[0])):
    column = [x[index] for x in lines]
    if column.count(".") == len(column):
        empty_columns.append(index)

def cal_distance(a_x,a_y,b_x,b_y):
    return abs(a_x - b_x)+abs(a_y - b_y)

def find_shortest_path(pos_a, pos_b, empty_rows, empty_columns):
    (a_x, a_y) = pos_a
    (b_x, b_y) = pos_b
    expansion = 0
    expansion_const = 999999
    for row in empty_rows:
        if a_x < b_x and row > a_x and row < b_x:
            expansion += expansion_const
        elif row < a_x and row > b_x:
            expansion += expansion_const
    for column in empty_columns:
        if a_y < b_y and column > a_y and column < b_y:
            expansion += expansion_const
        elif column < a_y and column > b_y:
            expansion += expansion_const
    return cal_distance(a_x, a_y, b_x, b_y) + expansion

max_x = len(lines)
max_y = len(lines[0])
galaxy_pos = []
for x in range(0, max_x):
    for y in range(0, max_y):
        if lines[x][y] == "#":
            galaxy_pos.append((x,y))

pairs = {}
for g1 in galaxy_pos:
    for g2 in galaxy_pos:
        if g1 == g2:
            continue
        if pairs.get((g2, g1)) is None:
            length = find_shortest_path(g1, g2, empty_rows, empty_columns)
            print(f'{g1} -> {g2}: {length}')
            pairs[(g1,g2)] = length
total = sum([x for x in pairs.values()])
print(total)