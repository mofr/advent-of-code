import assembunny

with open('day12_input_optimized') as f:
    input = f.read()

reg = assembunny.run(input, c=1)
print(reg['a'])
