input = open('input').read()

rope = [(0, 0)] * 10
visited = set()
for move in input.split('\n'):
    direction, step_count = move.split()
    step_count = int(step_count)
    for _ in range(step_count):
        x, y = rope[0]
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        rope[0] = x, y

        # Follow
        for i in range(1, len(rope)):
            x, y = rope[i - 1]
            tx, ty = rope[i]
            dx = x - tx
            dy = y - ty
            if dx > 1 and dy > 1:
                tx = x - 1
                ty = y - 1
            elif dx > 1 and dy < -1:
                tx = x - 1
                ty = y + 1
            elif dx < -1 and dy < -1:
                tx = x + 1
                ty = y + 1
            elif dx < -1 and dy > 1:
                tx = x + 1
                ty = y - 1
            elif dx > 1:
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
            rope[i - 1] = x, y
            rope[i] = tx, ty
        visited.add(rope[-1])

print(len(visited))
