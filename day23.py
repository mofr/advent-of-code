import assembunny

with open('day23_input_optimized') as f:
    input = f.read()

reg = assembunny.run(input, a=12)
print(reg['a'])
