
with open('/Users/cturner/workspace/advent-of-code-23/03/input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

# symbols = ['*', '#', '$', '+', '%', '/', '=', '-', '@', '&']
symbols = ['*']
max_x = len(lines)
max_y = len(lines[0])
    
found_parts = []
found_part_number = False
current_part = []

validate_part_index = set()
found_symbols = dict({})
for x in range(0,len(lines)):
    for y in range(0, len(lines[0])):
        if lines[x][y].isdigit():
            if found_part_number == False:
                found_part_number = True
            current_part.append((x,y))
        if not lines[x][y].isdigit() and found_part_number == True:
            found_parts.append(current_part)
            current_part = []
            found_part_number = False
        if lines[x][y] in symbols:
            found_symbols[(x,y)] =[
                (x+1,y-1),(x+1,y),(x+1,y+1),
                (x,y-1),(x,y+1),
                (x-1,y-1),(x-1,y),(x-1,y+1)
            ]

# total = 0
# for part in found_parts:
#     for index in part:
#         if index in validate_part_index:
#             x = 
#             total += int(x)
#             print(f'{x}')
#             break
total = 0
for (symbol, validate_part_index) in found_symbols.items():
    parts = []
    for part in found_parts:
      for index in part:
          if index in validate_part_index:
             parts.append(int(''.join([(lines[x][y]) for (x,y) in part])))
             break 
    if len(parts) == 2:
        total += parts[0] * parts[1]
    else:
        print("No enough parts")
        



print(len(found_parts))
print(validate_part_index)
print(total)