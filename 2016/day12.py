import sys

import assembunny

input_filename = sys.argv[1]

with open(input_filename + '_optimized') as f:
    input = f.read()

reg = assembunny.run(input, c=1)
print(reg['a'])
