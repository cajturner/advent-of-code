with open('/Users/cturner/personal/advent-of-code-23/15/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

instructions = lines[0].split(",")

total = 0

def hash(input):
    value = 0
    for c in input:
        value += ord(c)
        value *= 17
        value %= 256
    return value

def part1():
    for ins in instructions:
        total += hash(ins)
    print(total)

REMOVE = "remove"
ADD_REPLACE = "add_replace"

parsed_instructions = []
for ins in instructions:
    if ins.find("=") > -1:
        parsed_instructions.append([ADD_REPLACE] + ins.split("="))
    else:
        parsed_instructions.append([REMOVE] + ins.split("-"))

labels = dict()
boxes = dict()

for ins in parsed_instructions:
    operation, label, focal_length = ins
    box_index = hash(label)
    if operation == REMOVE:
        if boxes.get(box_index):
            if label in boxes.get(box_index):
                boxes[box_index].remove(label)
                del(labels[label])
    else:
        if not boxes.get(box_index):
            boxes[box_index] = [label]
            labels[label] = focal_length
        else:
            if label in boxes.get(box_index):
                labels[label] = focal_length
            else:
                boxes[box_index].append(label)
                labels[label] = focal_length
    print(f"boxes: {boxes}")
    print(f"labels: {labels}")
    print()

total = 0
for index, box in boxes.items():
    for i in range(len(box)):
        label = box[i]
        focus_power = (index + 1) * (i + 1) * int(labels[label])
        print(f"focus_power: {focus_power}")
        total += focus_power
print(total)
    