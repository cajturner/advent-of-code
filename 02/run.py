
with open('/Users/cturner/workspace/advent-of-code-23/02/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

max_dice = {
    'red': 12,
    'green': 13, 
    'blue': 14
}

games = { }
for line in lines:
    game, results = line.split(":")
    _sets = results.split(";")
    parsed_set = []
    for _set in _sets:
        parsed_dice = {}
        dice = _set.strip().split(', ')
        print(dice)
        for d in dice:
            number, colour = d.split(' ')
            parsed_dice[colour] = int(number)
        parsed_set.append(parsed_dice)
    games[int(game[5:])] = parsed_set

print(games)
def part1():
    possible_games = set(range(1, len(games)+1))
    for index, sets in games.items(): 
        isPossible = True
        for set in sets:
            for colour, count in set.items():
                if max_dice.get(colour) < count:
                    isPossible = False
                    possible_games.remove(index)
                    break
            if not isPossible:
                break
        
    print(possible_games)
    print(sum(possible_games))

def part2():
    total = 0
    for index, sets in games.items(): 
        min_dice = {
            'red': 0,
            'green': 0, 
            'blue': 0
        }  
        for set in sets:
            for colour, count in set.items():
                if count > min_dice[colour]:
                    min_dice[colour] = count
        total += min_dice['red'] * min_dice['green'] * min_dice['blue']
        
    print(total)
            
part2()