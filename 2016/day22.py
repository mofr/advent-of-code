from pathfinding import find_path
import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()


class Node:
    def __init__(self, line):
        splitted = line.split()
        self.size = int(splitted[1][:-1])
        self.used = int(splitted[2][:-1])
        self.avail = int(splitted[3][:-1])
        splitted = splitted[0].split('-')
        self.x = int(splitted[1][1:])
        self.y = int(splitted[2][1:])

nodes = {}
for line in input.split('\n')[2:]:
    node = Node(line)
    nodes[node.x, node.y] = node

width = max(nodes.values(), key=lambda node: node.x).x + 1
height = max(nodes.values(), key=lambda node: node.y).y + 1
empty_node = [node for node in nodes.values() if node.used == 0][0]

goal = width - 1, 0
next_goal = None
def passable(src, dst):
    if dst[0] < 0 or dst[1] < 0 or dst[0] >= width or dst[1] >= height:
        return False
    if dst == goal and src != next_goal:
        return False
    if nodes[dst].size < nodes[src].used:
        return False
    return True
goal_path = find_path(goal, (0, 0), passable)
empty = empty_node.x, empty_node.y
move_count = 0
for goal, next_goal in zip(goal_path, goal_path[1:]):
    path = find_path(empty, goal, passable)
    empty = goal
    move_count += len(path) - 1
print(move_count)
