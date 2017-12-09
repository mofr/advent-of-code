import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()


class Disc:
    def __init__(self, pos, count):
        self.pos = pos
        self.count = count

discs = []

for i, line in enumerate(input.split('\n')):
    splitted = line.split()
    count = int(splitted[3])
    pos = (int(splitted[-1][:-1]) + i + 1) % count
    discs.append(Disc(pos, count))

time = 0
while True:
    for disc in discs:
        if (disc.pos + time) % disc.count != 0:
            break
    else:
        break

    time += 1

print(time)
