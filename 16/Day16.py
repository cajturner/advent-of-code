with open('/Users/cturner/personal/advent-of-code-23/16/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

EMPTY_SPACE = "."
DOWN_MIRROR = "\\"
UP_MIRROR = "/"
VERTICAL_SPLITTER = "|"
HORIZONTAL_SPLITTER = "-"

max_index= len(lines)-1
start_locations = []
for x in range(len(lines)):
    start_locations.append((x, -1, RIGHT))
    start_locations.append((x,max_index+1 , LEFT))
for y in range(len(lines)):
    start_locations.append((-1, y, DOWN))
    start_locations.append((max_index+1, y, UP))


def get_next_tile(x, y, direction, max_x, max_y):
    if direction == RIGHT:
        if y == max_y :
            return None
        return x, y+1
    elif direction == LEFT:
        if y == 0:
            return None
        return x, y-1
    elif direction == UP:
        if x == 0:
            return None
        return x-1, y
    elif direction == DOWN:
        if x == max_x:
            return None
        return x+1, y
    
def evaluate_start(start_x,start_y,start_direction):
    beams = [(start_x,start_y,start_direction)]
    energized_tiles = set()
    energized_tiles_w_direction = set()
    while len(beams) > 0:
        new_beams = []
        for beam in beams:
            # for x in range(len(lines)):
            #     for y in range(len(lines[x])):
            #         if (x,y) in energized_tiles:
            #             print("#", end="")
            #         else:
            #             print(lines[x][y], end="")
            #     print()
            # print()
            x,y,direction = beam
            next_tile_coords = get_next_tile(x, y, direction, max_index, max_index)
            if next_tile_coords is None:
                continue 
            elif (next_tile_coords[0], next_tile_coords[1], direction) in energized_tiles_w_direction:
                continue
            next_x, next_y = next_tile_coords
            energized_tiles.add((next_x, next_y))
            energized_tiles_w_direction.add((next_x, next_y, direction))
            next_tile = lines[next_x][next_y]
            if next_tile == EMPTY_SPACE:
                new_beams.append((next_x, next_y, direction))
            elif next_tile == HORIZONTAL_SPLITTER:
                if direction in [LEFT, RIGHT]:
                    new_beams.append((next_x, next_y, direction))
                else:
                    new_beams.append((next_x, next_y, LEFT))
                    new_beams.append((next_x, next_y, RIGHT))
            elif next_tile == VERTICAL_SPLITTER:
                if direction in [UP, DOWN]:
                    new_beams.append((next_x, next_y, direction))
                else:
                    new_beams.append((next_x, next_y, UP))
                    new_beams.append((next_x, next_y, DOWN))
            elif next_tile == UP_MIRROR: # /
                if direction == RIGHT:
                    new_beams.append((next_x, next_y, UP))
                elif direction == DOWN:
                    new_beams.append((next_x, next_y, LEFT))
                elif direction == UP:
                    new_beams.append((next_x, next_y, RIGHT))
                elif direction == LEFT:
                    new_beams.append((next_x, next_y, DOWN))
            elif next_tile == DOWN_MIRROR: # \
                if direction == RIGHT:
                    new_beams.append((next_x, next_y, DOWN))
                elif direction == UP:
                    new_beams.append((next_x, next_y, LEFT))
                elif direction == DOWN:
                    new_beams.append((next_x, next_y, RIGHT))
                elif direction == LEFT:
                    new_beams.append((next_x, next_y, UP))
        beams = new_beams
    return len(energized_tiles)

max_energized_tiles = 0
for start_location in start_locations:
    value = evaluate_start(*start_location)
    print(f"{start_location} - {value}")
    if max_energized_tiles < value:
        max_energized_tiles = value
print(max_energized_tiles)