import itertools
from functools import lru_cache
from pathfinding import find_path

with open('day24_input') as f:
    input = f.read()

lines = []
for line in input.split('\n'):
    lines.append(line)

@lru_cache()
def find_pos(pos):
    for row, line in enumerate(lines):
        if pos in line:
            return line.index(pos), row

def passable(src, dst):
    return lines[dst[1]][dst[0]] != '#'

targets = []
for c in input:
    if c.isdigit() and c != '0':
        targets.append(c)

find_path = lru_cache()(find_path)
route_lenths = []
for route in itertools.permutations(targets):
    pos = find_pos('0')
    route_length = 0
    route = list(route) + ['0']
    for i in route:
        target = find_pos(i)
        route_length += len(find_path(pos, target, passable)) - 1
        pos = target
    route_lenths.append(route_length)

print(min(route_lenths))
