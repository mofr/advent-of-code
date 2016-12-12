with open('day12_input_optimized') as f:
    input = f.read()

statements = list(map(lambda s: (s.split()[0], s.split()[1:]), input.split('\n')))

pc = 0
reg = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0,
}

def val(arg):
    if arg in reg:
        return reg[arg]
    else:
        return int(arg)

while pc < len(statements):
    op, args = statements[pc]
    if op == 'cpy':
        reg[args[1]] = val(args[0])
    elif op == 'inc':
        reg[args[0]] += 1
    elif op == 'dec':
        reg[args[0]] -= 1
    elif op == 'jnz':
        if val(args[0]) != 0:
            pc += int(args[1])
            continue
    elif op == 'add':
        reg[args[1]] += reg[args[0]]
    else:
        raise
    pc += 1

print(reg['a'])
