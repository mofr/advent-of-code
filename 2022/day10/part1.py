input = open('input').read()

x = 1
cycles = [x]
for instruction in input.split('\n'):
    if instruction.startswith('addx'):
        cycles.append(x)
        cycles.append(x)
        add_, dx = instruction.split()
        x += int(dx)
    if instruction.startswith('noop'):
        cycles.append(x)

checkpoints = [20, 60, 100, 140, 180, 220]
print(sum((c * cycles[c] for c in checkpoints)))
