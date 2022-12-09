input = open('input').read()

grid = input.split()
for i in range(len(grid)):
    grid[i] = list(map(int, grid[i]))

h = len(grid)
w = len(grid[0])
visible = set()

# Horizontal scan
for y in range(h):
    for x_range in [range(w), range(w - 1, -1, -1)]:
        max_height = -1
        for x in x_range:
            if grid[y][x] > max_height:
                visible.add((x, y))
                max_height = grid[y][x]

# Vertical scan
for x in range(w):
    for y_range in [range(h), range(h - 1, -1, -1)]:
        max_height = -1
        for y in y_range:
            if grid[y][x] > max_height:
                visible.add((x, y))
                max_height = grid[y][x]

print(len(visible))
