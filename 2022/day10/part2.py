input = open('input').read()

x = 1
cycles = [x]
for instruction in input.split('\n'):
    if instruction.startswith('addx'):
        cycles.append(x)
        add_, dx = instruction.split()
        x += int(dx)
        cycles.append(x)
    if instruction.startswith('noop'):
        cycles.append(x)

w = 40
screen = [
    '#' if i % 40 in (x - 1, x, x + 1) else ' '
    for i, x in enumerate(cycles)
]
screen = ''.join(screen)
for offset in range(0, len(cycles), w):
    print(screen[offset:offset+w])
