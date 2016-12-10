from collections import defaultdict

with open('day10_input') as f:
    input = f.read()

chips = defaultdict(list)
output = []
instructions = input.split('\n')


def reserve(lst, count):
    while len(lst) < count:
        lst.append(None)

while len(instructions) > 0:
    for line in list(instructions):
        splitted = line.split()
        if splitted[0] == 'value':
            bot = int(splitted[-1])
            value = int(splitted[1])
            chips[bot].append(value)
        elif splitted[0] == 'bot':
            bot = int(splitted[1])
            low_to = int(splitted[6])
            high_to = int(splitted[-1])
            dst_lo = splitted[5]
            dst_hi = splitted[-2]

            if len(chips[bot]) < 2:
                continue

            lo, hi = min(chips[bot]), max(chips[bot])
            chips[bot] = []

            if (lo, hi) == (17, 61):
                print(bot)

            if dst_hi == 'output':
                reserve(output, high_to + 1)
                output[high_to] = hi
            else:
                chips[high_to].append(hi)

            if dst_lo == 'output':
                reserve(output, low_to + 1)
                output[low_to] = lo
            else:
                chips[low_to].append(lo)
        instructions.remove(line)

print(output[0] * output[1] * output[2])

