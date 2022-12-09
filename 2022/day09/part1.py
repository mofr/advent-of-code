input = open('example').read()

x, y = 0, 0
tx, ty = 0, 0
visited = set()
for move in input.split('\n'):
    direction, step_count = move.split()
    step_count = int(step_count)
    for _ in range(step_count):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1

        dx = x - tx
        dy = y - ty
        if dx > 1:
            tx = x - 1
            ty = y
        elif dx < -1:
            tx = x + 1
            ty = y
        elif dy > 1:
            ty = y - 1
            tx = x
        elif dy < -1:
            ty = y + 1
            tx = x
        visited.add((tx, ty))

print(len(visited))
