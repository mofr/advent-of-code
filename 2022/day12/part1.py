input = open('input').read()

grid = list(map(list, input.strip().split()))
start_pos = (0, 0)
goal_pos = (0, 0)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == 'S':
            start_pos = (x, y)
            row[x] = 'a'
        if c == 'E':
            goal_pos = (x, y)
            row[x] = 'z'
grid = [list(map(ord, row)) for row in grid]

w = len(grid[0])
h = len(grid)
wave = {start_pos}
visited = {start_pos}
step_count = 0
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
for step_count in range(1000000):
    if goal_pos in wave:
        print(step_count)
        break
    new_wave = set()
    for x, y in wave:
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if grid[ny][nx] - grid[y][x] > 1:
                continue
            new_wave.add((nx, ny))
    wave = new_wave - visited
