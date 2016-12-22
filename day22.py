with open('day22_input') as f:
    input = f.read()


def find_path(src, target, passable):
    """
    >>> path = find_path((1, 1), (3, 4), lambda: True)
    >>> len(path)
    6
    >>> find_path((1, 1), (3, 1), lambda: True)
    [(1, 1), (2, 1), (3, 1)]

    :rtype: list or None if not found
    """
    paths = [[src]]
    visited = {src}
    # search until target is reached or all possible paths are discovered
    while len(paths) > 0:
        current_paths = paths
        paths = []
        for path in current_paths:
            for step in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                p = path[-1]
                dst = p[0] + step[0], p[1] + step[1]
                if passable(p, dst) and dst not in visited:
                    new_path = path.copy()
                    new_path.append(dst)
                    paths.append(new_path)
                    visited.add(dst)
                    if dst == target:
                        return new_path
    return None


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
