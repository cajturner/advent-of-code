with open('/Users/cturner/personal/advent-of-code-23/13/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

patterns = [[]]
i = 0
for line in lines:
    if line == "":
        patterns.append([])
        i+=1
    else:
        patterns[i].append(line)

def check_reflection(patterns, index, reflection_size):
    pattern_a = patterns[index-reflection_size:index]
    pattern_b = list(reversed(patterns[index:row_i+reflection_size]))
    found_smudge = False
    if pattern_a != pattern_b:
        differences = sum(a != b for a, b in zip(pattern_a[0], pattern_b[0]))
        if differences == 1:
            found_smudge = True
            patterns = patterns[:index-reflection_size] + [pattern_b[0]] + patterns[index-reflection_size+1:]
        else:
            return False, 0, found_smudge
        
    if index-reflection_size == 0 or index+reflection_size == len(patterns):
        return True, reflection_size, found_smudge
    else:
        result, new_reflection_size, returned_smudge = check_reflection(patterns, index, reflection_size+1)
        if result: 
            return result, new_reflection_size, found_smudge if found_smudge else returned_smudge
    return False, 0, returned_smudge
  

total = 0
for pattern in patterns:
    reflection_size = 1
    horizontal=0
    horizontal_row_i = 0
    for row_i in range(1, len(pattern)):
        result, value, found_smudge = check_reflection(pattern, row_i, reflection_size)
        if result and found_smudge:
            if value >= horizontal:
                horizontal_row_i = row_i
                horizontal = value

    vertical = 0

    transposed_lines = ["".join(list(x)) for x in zip(*pattern)]
    reflection_size = 1
    vertical_row_i = 0
    for row_i in range(1, len(transposed_lines)):
        result, value, found_smudge = check_reflection(transposed_lines, row_i, reflection_size)
        if result and found_smudge:
            if value >= vertical:
                vertical_row_i = row_i
                vertical = value
    if horizontal == 0 and vertical == 0:
        print("NO")
        print(pattern)

    if horizontal > vertical:
        print(f"VH - {100*horizontal_row_i}")
        total += 100 * horizontal_row_i
    else:
        print(f"VV - {vertical_row_i}")
        total += vertical_row_i
print(total)
