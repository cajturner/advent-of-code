

with open('/Users/cturner/workspace/advent-of-code-23/01/test.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def part1(lines):
    digits = []

    for line in lines:
        x = []
        for character in line:
            if character.isdigit():
                x.append(character)
                break
        for character in reversed(line):
            if character.isdigit():
                x.append(character)
                break
        digits.append(int(x[0]+x[1]))
        
    print(sum(digits))


def part2(lines):
    words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    digits = []

    for line in lines:
        x = []
        for word in words.keys():
            if line.startswith(word):
                x.append(words.get(word))
                break
        if len(x)==0: 
            for i in range(0,len(line)+1):
                if line[i].isdigit():
                    x.append(line[i])
                    break
                else:
                    sub_line = line[i:]
                    for word in words.keys():
                        if sub_line.startswith(word):
                            x.append(words.get(word))
                            break
                    if len(x)>0:
                        break

        for word in words.keys():
            if line.endswith(word):
                x.append(words.get(word))
                break    
        if len(x)==1:    
            for i in range(len(line)-1, -1, -1):
                if line[i].isdigit():
                    x.append(line[i])
                    break
                else:
                    sub_line = line[:i]
                    for word in words.keys():
                        if sub_line.endswith(word):
                            x.append(words.get(word))
                            break
                    if len(x)>1:
                        break

        digits.append(int(x[0]+x[1]))
    print(digits)
    print(sum(digits))

part1(lines)
part2(lines)