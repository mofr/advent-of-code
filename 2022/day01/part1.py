import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

max_total = 0
for elf in input.split('\n\n'):
    elf_total = sum(map(int, elf.split('\n')))
    if elf_total > max_total:
        max_total = elf_total

print(max_total)
