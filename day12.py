from assembunny import Assembunny

with open('day12_input_optimized') as f:
    input = f.read()

asm = Assembunny(input, c=1)
asm.run()
print(asm.reg['a'])
