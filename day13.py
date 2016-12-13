favorite_number = 1364


def wall(x, y):
    return '{0:b}'.format(x*x + 3*x + 2*x*y + y + y*y + favorite_number).count('1') % 2 == 1


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = wall(x, y)
        self.char = '#' if self.wall else '.'
        self.step = None

    def step_on(self, step):
        if self.step is not None:
            return
        if self.wall:
            return
        self.step = step


class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.data = []
        for y in range(self.y):
            row = []
            for x in range(self.x):
                row.append(Cell(x, y))
            self.data.append(row)

    def __getitem__(self, pos):
        x, y = pos
        return self.data[y][x]

    def __iter__(self):
        for row in self.data:
            for cell in row:
                yield cell


def wave(grid, target):
    for cell in grid:
        cell.step = None
    grid[target].step = 0

    step = 0
    finished = False
    while not finished:
        step += 1
        finished = True
        for cell in grid:
            x, y = cell.x, cell.y
            if cell.step == step - 1:
                grid[max(0, x - 1), y].step_on(step)
                grid[min(x + 1, grid.x-1), y].step_on(step)
                grid[x, max(0, y - 1)].step_on(step)
                grid[x, min(y + 1, grid.y - 1)].step_on(step)
                finished = False


grid = Grid(50, 50)
grid[0, 0].wall = False
wave(grid, [31, 39])
print(grid[0, 0].step)

wave(grid, [0, 0])
count_50 = 0
for cell in grid:
    if type(cell.step) is int and cell.step < 50:
        count_50 += 1
print(count_50)
