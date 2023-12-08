
with open('/Users/cturner/workspace/advent-of-code-23/04/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

cards = {}
for line in lines:
    index, values = line.split(': ')

    winning, numbers = values.split(' | ')
    parsed_win = [win.strip("") for win in winning.split(" ") if win != '']
    parsed_num = [num.strip("") for num in numbers.split(" ") if num != '']
    cards[int(index[5:])] = (set(parsed_win), set(parsed_num))

total = 0
copies = {}
for card_i, (winning, numbers) in cards.items():
    matches = winning.intersection(numbers)
    if matches:
        for i in range(1,len(matches)+1):
            if copies.get(card_i + i) is None:
                copies[card_i + i] = 1
            else:
                copies[card_i + i] += 1
    if copies.get(card_i):
        for i in range(0, copies.get(card_i)):
            for i in range(1,len(matches)+1):
                if copies.get(card_i + i) is None:
                    copies[card_i + i] = 1
                else:
                    copies[card_i + i] += 1

print(len(cards) + sum(copies.values()))

