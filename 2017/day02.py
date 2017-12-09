import itertools
import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

checksum = 0
for line in input.split('\n'):
    line = line.strip()
    for a, b in itertools.product(line.split(), repeat=2):
        if a == b:
            continue
        a = int(a)
        b = int(b)
        if a % b == 0:
            checksum += a // b
            break

print(checksum)
