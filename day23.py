from assembunny import Assembunny

with open('day23_input_optimized') as f:
    input = f.read()

asm = Assembunny(input, a=12)
asm.run()
print(asm.reg['a'])
