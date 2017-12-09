import assembunny
import sys

input_filename = sys.argv[1]

with open(input_filename + '_optimized') as f:
    input = f.read()

reg = assembunny.run(input, a=12)
print(reg['a'])
