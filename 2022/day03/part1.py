import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()


def prio(item):
    o = ord(item)
    return o - 96 if o > 96 else o - 38


total = 0
for rucksack in input.strip().split('\n'):
    rucksack = rucksack.strip()
    c1 = rucksack[:len(rucksack) // 2]
    c2 = rucksack[len(rucksack) // 2:]
    duplicates = set(c1) & set(c2)
    total += sum(map(prio, duplicates))


print(total)
