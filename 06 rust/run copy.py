from functools import reduce
import time
with open('/Users/cturner/workspace/advent-of-code-23/06/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


race_duration = [int(x) for x in lines[0][6:].strip().split(" ") if x != '']
race_record = [int(x) for x in lines[1][10:].strip().split(" ") if x != '']

def is_winning_way(race_duration, race_record, button_push_time):
    remaining_time = race_duration - button_push_time
    total_dist = remaining_time * button_push_time
    if total_dist > race_record:
        return True
    return False

def find_winning_ways(race_duration, race_record):
    min_win = None
    max_win = None

    found_min = False
    current_push_time = int(race_duration/2)
    while not found_min:
        is_winning = is_winning_way(race_duration, race_record, current_push_time)
        if is_winning:
            current_push_time = int(current_push_time / 2)
        else:
            while not is_winning_way(race_duration, race_record, current_push_time):
                current_push_time +=1
            min_win = current_push_time
            found_min = True

    found_max = False
    current_push_time = int(race_duration/2)
    offset = current_push_time
    while not found_max:
        is_winning = is_winning_way(race_duration, race_record, current_push_time)
        if is_winning:
            current_push_time = offset + int(current_push_time / 2)
        else:
            while not is_winning_way(race_duration, race_record, current_push_time):
                current_push_time -=1
            max_win = current_push_time+1
            found_max = True
    print(f'total: {max_win-min_win}')

part2_race_duration = int(lines[0][6:].replace(" ", ''))
part2_race_record = int(lines[1][10:].replace(" ", ''))
start = time.time()
find_winning_ways(part2_race_duration, part2_race_record)
end = time.time()
print(end-start)