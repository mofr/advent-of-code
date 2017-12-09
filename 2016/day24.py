import sys
import itertools
from functools import lru_cache

from pathfinding import find_path

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

lines = []
for line in input.split('\n'):
    lines.append(line)


def find_pos(pos):
    for row, line in enumerate(lines):
        if pos in line:
            return line.index(pos), row


def passable(src, dst):
    return lines[dst[1]][dst[0]] != '#'

checkpoints = []
for c in input:
    if c.isdigit() and c != '0':
        checkpoints.append(find_pos(c))

find_path = lru_cache()(find_path)
route_lenths = []
for route in itertools.permutations(checkpoints):
    pos = find_pos('0')
    route_length = 0
    route = list(route) + [pos]
    for checkpoint in route:
        route_length += len(find_path(pos, checkpoint, passable)) - 1
        pos = checkpoint
    route_lenths.append(route_length)

print(min(route_lenths))
