input = open('input').read()

grid = input.split()
for i in range(len(grid)):
    grid[i] = list(map(int, grid[i]))

h = len(grid)
w = len(grid[0])
max_score = 0

for y in range(h):
    for x in range(w):
        score = 1

        visible_count = 0
        for scan_x in range(x + 1, w):
            visible_count += 1
            if grid[y][scan_x] >= grid[y][x]:
                break
        score *= visible_count

        visible_count = 0
        for scan_x in range(x - 1, -1, -1):
            visible_count += 1
            if grid[y][scan_x] >= grid[y][x]:
                break
        score *= visible_count

        visible_count = 0
        for scan_y in range(y + 1, h):
            visible_count += 1
            if grid[scan_y][x] >= grid[y][x]:
                break
        score *= visible_count

        visible_count = 0
        for scan_y in range(y - 1, -1, -1):
            visible_count += 1
            if grid[scan_y][x] >= grid[y][x]:
                break
        score *= visible_count

        if score > max_score:
            max_score = score

print(max_score)
