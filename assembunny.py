class Assembunny:
    def __init__(self, source, **registers):
        self.statements = list(map(lambda s: [s.split()[0], s.split()[1:]], source.split('\n')))
        self.pc = 0
        self.reg = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
        }
        self.reg.update(registers)

    def run(self, out=None):
        while self.pc < len(self.statements):
            op, args = self.statements[self.pc]
            if op == 'cpy':
                self.reg[args[1]] = self.val(args[0])
            elif op == 'inc':
                self.reg[args[0]] += 1
            elif op == 'dec':
                self.reg[args[0]] -= 1
            elif op == 'jnz':
                if self.val(args[0]) != 0:
                    self.pc += self.val(args[1])
                    continue
            elif op == 'add':
                self.reg[args[1]] += self.val(args[0])
            elif op == 'addmult':
                self.reg[args[2]] += self.val(args[0]) * self.val(args[1])
            elif op == 'out':
                if out(self.val(args[0])):
                    break
            elif op == 'tgl':
                index = self.val(args[0]) + self.pc
                if 0 <= index < len(self.statements):
                    op, args = self.statements[index]
                    if len(args) == 1:
                        self.statements[index][0] = 'dec' if op == 'inc' else 'inc'
                    else:
                        self.statements[index][0] = 'cpy' if op == 'jnz' else 'jnz'
            else:
                raise Exception("Unknown instruction {} at line {}".format(op, self.pc))
            self.pc += 1

    def val(self, arg):
        if arg in self.reg:
            return self.reg[arg]
        else:
            return int(arg)