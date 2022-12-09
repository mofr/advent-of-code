import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()


def calc_elf(i) -> int:
    return sum(map(int, i.split('\n')))


elves = sorted(map(calc_elf, input.split('\n\n')))
print(sum(elves[-3:]))
