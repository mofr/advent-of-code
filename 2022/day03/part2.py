import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()


def prio(item):
    o = ord(item)
    return o - 96 if o > 96 else o - 38


total = 0
rucksacks = input.strip().split('\n')
for i in range(0, len(rucksacks), 3):
    r1 = rucksacks[i]
    r2 = rucksacks[i + 1]
    r3 = rucksacks[i + 2]
    common_items = set(r1) & set(r2) & set(r3)
    total += sum(map(prio, common_items))

print(total)
