with open('day8_input') as f:
    input = f.read()

screen = []
for _ in range(6):
    row = []
    for _ in range(50):
        row.append('.')
    screen.append(row)

def count(screen):
    result = 0
    for row in screen:
        result += row.count('#')
    return result

def rotate(l, n):
    return l[-n:] + l[:-n]

for line in input.split('\n'):
    if line.startswith('rect'):
        rect_x, rect_y = map(int, line.split()[1].split('x'))
        for y in range(rect_y):
            for x in range(rect_x):
                screen[y][x] = '#'
    elif line.startswith('rotate column'):
        shift = int(line.split(' ')[4])
        x = int(line.split(' ')[2].split('=')[1])
        tmp = []
        for y in range(6):
            tmp.append(screen[y][x])
        tmp = rotate(tmp, shift)
        for y in range(6):
            screen[y][x] = tmp[y]
    elif line.startswith('rotate row'):
        shift = int(line.split(' ')[4])
        y = int(line.split(' ')[2].split('=')[1])
        screen[y] = rotate(screen[y], shift)

print(count(screen))

for y in range(6):
    print(''.join(screen[y]))
