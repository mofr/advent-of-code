def run(source, out=None, **registers):
    statements = list(map(lambda s: [s.split()[0], s.split()[1:]], source.split('\n')))
    pc = 0
    reg = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
    }
    reg.update(registers)

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
                pc += val(args[1])
                continue
        elif op == 'add':
            reg[args[1]] += val(args[0])
        elif op == 'addmult':
            reg[args[2]] += val(args[0]) * val(args[1])
        elif op == 'out':
            if out(val(args[0])):
                break
        elif op == 'tgl':
            index = val(args[0]) + pc
            if 0 <= index < len(statements):
                op, args = statements[index]
                if len(args) == 1:
                    statements[index][0] = 'dec' if op == 'inc' else 'inc'
                else:
                    statements[index][0] = 'cpy' if op == 'jnz' else 'jnz'
        else:
            raise Exception("Unknown instruction {} at line {}".format(op, pc))
        pc += 1

    return reg
